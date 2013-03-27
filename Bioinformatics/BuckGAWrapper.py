#This can be run in a local machine
import os, stat, subprocess, sys, commands, time
from multiprocessing import Lock, Value
from pyevolve import G1DBinaryString
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators




def runGeneMania(cmd):
    p = subprocess.call(cmd, shell=True)
   # os.system(cmd)
    
def getNetworks(fileName):
    networks = [network.strip() for network in open(fileName)]
    return networks


def retrieveAUROC(fileName):
    f = open(fileName, "r+b")
    score = 0.0
    num   = 0
    for line in f:
        index = line.find("\t-\t")
        if index != -1:
            score += foat(line[index+3:line.find("\t", index+3, len(line))])
            num    = num + 1
    if num != 0:
        score = score / num;
    f.close()
    return score
        
def verify_task_done(result_file):
    modify_time    = 0
    last_m_time    = 0
    qsub_wait_time = 120
    gm_wait_time   = 600
    max_wait_time  = 60
    is_job_doing   = False
    duration       = 0
    poll_interval  = 1
    score          = 0.0
    #print result_file
    while duration < qsub_wait_time:
        time.sleep(poll_interval)
        duration   += poll_interval
        #last_m_time = modify_time
        #if os.path.exists(result_file):
        #    modify_time = os.stat(result_file).st_mtime
        #if modify_time != last_m_time:
        #    duration = 0
        #else:
        #    if os.path.exists(result_file):
        #        #score = retrieveAUROC(result_file)
        #        f = open(result_file)
        #        for line in f:
        #            score = float(line.strip())
        #            print score
        #        f.close()
        #        if score > 0:
        #            break
        if os.path.exists(result_file):
                #score = retrieveAUROC(result_file)
                is_job_doing = True
                break
                #f = open(result_file)
                #for line in f:
                #    score = float(line.strip())
                #    print score
                #f.close()
                #if score > 0:
                #    break
    duration = 0
    while is_job_doing and duration < gm_wait_time:
        time.sleep(poll_interval)
        duration += poll_interval
        if os.path.getsize(result_file) > 0:
            f = open(result_file)
            for line in f:
                score = float(line.strip())
                print score
            f.close()
            break
            
    if is_job_doing == False:
        return 0
    else: 
        return score
    #if duration < max_wait_time:
    #    return score
    #else:
    #    if os.path.exists(result_file):
    #        return 0
    #    else:
    #        return -1

def get_task_id():
    global job_id, generation_id, individual_id
    global population_size
    task_id = "job_%s_%s_%s" % (job_id, generation_id, individual_id)
    individual_id = individual_id + 1
    if individual_id == population_size:
        generation_id += 1
        individual_id  = 0
    return task_id

def evolve_callback(ga_engine):
    global top5_score, top5_networks, best_individuals, avg_individuals, top5_individual
    internal_pop = ga_engine.getPopulation()
    #avg_individuals.append(ga_engine.getStatistics()["rawAve"])
    best_individuals.append(ga_engine.bestIndividual().score)
    avg_score = 0.0
    ind_num   = 0
    for ind in internal_pop:
        if ind.score > 0:
            avg_score += ind.score
            ind_num   += 1
            top5_individual.update({ind.score:ind.getBinary()})
        #if len(top5_score) < 5:
        #    top5_score.append(ind.score)
        #    top5_networks.append(ind.getBinary())
        #else:
        #    for i in range(5):
        #        if ind.score == top5_score[i]:
        #            continue
        #        if ind.score > top5_score[i]:
        #            top5_score[i] = ind.score
        #            top5_networks[i] = ind.getBinary()
        #            break
    if ind_num > 0:
        avg_score /= ind_num
    avg_individuals.append(avg_score)


def eval_func(chromosome):
    global all_network_list, java_path, population_size
    global geneMANIA_dir, organism, test_gene
    global results_dir, generation_id, individual_id, job_id
    cur_network_list = [];
    #l.acquire()
    task_id = "job_%s_%s_%s" % (job_id, generation_id.value, individual_id.value)
    individual_id.value += 1
    if individual_id.value == population_size:
        generation_id.value += 1
        individual_id.value  = 0
    #print task_id
    #l.release()
    for i in range(0, len(all_network_list)):
        if chromosome[i] == 1:
            cur_network_list.append(all_network_list[i])
    cur_network_list = ",".join(cur_network_list)
    tmp_result_file  = results_dir + "avg_" + task_id + ".txt"
#    cmd = java_path + " -Xmx1800M -cp " + geneMANIA_dir + "*.jar org.genemania.plugin.apps.CrossValidator " + \
#             "--data " + geneMANIA_dir + "gmdata-2012-08-02 --organism " + "\"H. Sapiens\"" + " --query " + test_gene + \
#             " --networks " + cur_network_list + " --auto-negatives --folds 3 --outfile " + tmp_result_file
#    runGeneMania(cmd)
    #print cur_network_list
    #p = os.system("sh geneMANIA_job.sh " +"\"" + cur_network_list  + "\""+ " " + task_id) 
    p = os.system("qsub -cwd -l hostname='compute-0-0|compute-0-1|compute-0-2|compute-0-3|compute-0-4|compute-0-5|compute-0-6|compute-0-7|compute-0-8|compute-0-9',mem_free=7G,num_proc=8 -pe orte 1 -o /home/sfeng/cs640/Results/qsub_$job_id.txt -e /home/sfeng/cs640/Results/qsub_error_" + task_id +" -S /bin/bash -N " + task_id + " geneMANIA_job.sh " + "\"" + cur_network_list + "\"" + " " + task_id)
    result = verify_task_done(tmp_result_file)
    if result > 0:
        return result
    else:
        return 0.0

def get_network_list():
    '''
    Get a list of available biological network by organism type
    '''
    global geneMANIA_dir, organism, gene_set_dir
    global java_path
    gm_data = geneMANIA_dir + "gmdata-2012-08-02"
    query   = gene_set_dir + "yeast.query"    
    cmd     = java_path + " -cp " + geneMANIA_dir + "*.jar org.genemania.plugin.apps.QueryRunner --data " + gm_data + " --list-networks " + \
                 organism + " " + query
    p = commands.getoutput(cmd)  
    #print p  
    all_network_list = []
    if p is not None:
        all_network_list = [network.strip() for network in p.split('\n')]
    return all_network_list

def run_GA():
    global all_network_list
    global population_size, generation_num
    networks_num = len(all_network_list)
    genome       = G1DBinaryString.G1DBinaryString(networks_num)


    genome.evaluator.set(eval_func)
    genome.mutator.set(Mutators.G1DBinaryStringMutatorFlip)


    ga = GSimpleGA.GSimpleGA(genome)
    ga.selector.set(Selectors.GTournamentSelector)
    ga.setMultiProcessing(flag=True)
    ga.setPopulationSize(population_size)
    ga.setGenerations(generation_num)
    ga.stepCallback.set(evolve_callback)
    
    ga.evolve(freq_stats=1)
    best = ga.bestIndividual()


    print best

def main():
    argv     = sys.argv
    if len(argv) != 4:
        print "Usage: python GAWrapper.py [test gene file name]" + \
            " [\"organism\"] [job_id]\n" 
        sys.exit(1)
    global work_dir, java_path, gene_set_dir
    global geneMANIA_dir, results_dir
    global test_gene, organism, all_network_list
    global population_size, generation_num
    global job_id, generation_id, individual_id
    global lock
    global top5_score 
    global top5_networks
    global best_individuals
    global avg_individuals
    global top5_individual
    top5_individual = {}
    avg_individuals = []
    top5_score      = []
    top5_networks   = []
    best_individuals = []
    job_id        = argv[3]
    generation_id = Value('i', 0)
    individual_id = Value('i', 0)
    work_dir      = "/home/sfeng/cs640/"
    java_path     = "/usr/java/latest/bin/java"
    gene_set_dir  = work_dir + "GeneSet/"
    geneMANIA_dir = work_dir + "GeneMANIA/" 
    results_dir   = work_dir + "Results/GeneSets_1009_human_gene_100_5_100_withBackground/"
    test_gene     = gene_set_dir + argv[1]
    organism      = "\"" + argv[2] + "\""
    networks_dir  = work_dir + "Networks/"
    #all_network_list  = get_network_list()
    population_size   = 20
    generation_num    = 50
    all_network_list = getNetworks(networks_dir + "human_network.txt")
    #print "%s\n" % len(all_network_list)
    #print all_network_list
    if not all_network_list:
        print "Can not get network list!\n"
        sys.exit(1)
    run_GA()
    num = 0
    for key in sorted(top5_individual.iterkeys(), reverse=True):
        print "%s, %s\n" % (key, top5_individual[key])
        num += 1
        if num == 5:
            break
    #print top5_score 
    #print "\n"
    #print top5_networks
    #print "\n"
    print best_individuals
    print "\n"
    print avg_individuals

if __name__ == "__main__":
    main()
