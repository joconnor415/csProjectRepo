function matcher(event){
            var username = document.getElementById("user").value;
            var pw = document.getElementById("pwd").value;
            var confirm_pw = document.getElementById("cpwd").value;

            if ((pw == confirm_pw) && username){
                handler(username, pw);
            }
            else{
                alert('Please check the username and password you entered');
                window.location = "register.php";
            }
        }
        
        function handler(username, password) {
            
            var pubkeyContent = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRF/CQAFt72U3bzS+RSQH9M23nmChMktHDJZtVdh60w2EUfVaB8rYRzub6aakdJh151Yl78Bwi29om84FeVhNn4i3u21J0u7RgT4S1aABGU1V31AFZFO+bEAktpnAGuKuOLPtFppaOmZgiLmHPwJw8UyYqoyRStFoUET/nDkH+qQIDAQAB-----END PUBLIC KEY-----";
            var pubk = RSA.getPublicKey(pubkeyContent);
            var user = username;
            var pw = password;
            var time = String(new Date().getTime());
            var encryptedPass = RSA.encrypt(time+sha1(pw), pubk);
    
            var pform = document.createElement('form');
            pform.action = 'register.php';
            pform.method = 'post';
            var p = document.createElement('input');
            p.type = 'hidden';
            p.name = 'p';
            p.value = encryptedPass;
            pform.appendChild(p);
            var u = document.createElement('input');
            u.type = 'hidden';
            u.name = 'u';
            u.value = user;
            pform.appendChild(u);
            var ts = document.createElement('input');
            ts.type = 'hidden';
            ts.name = 'ts';
            ts.value = time;
            pform.appendChild(ts);
            document.getElementById('encryption').appendChild(pform);
            
            pform.submit();
        }