using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace FinalShooter
{
    public class SoundManager
    {
     
        public SoundEffect playerShootSound;
        public SoundEffect explodeSound;
        public SoundEffect bombSound;
        public SoundEffect missileLaunchSound;
       
        public Song gameMusic;
        public Song gunsNRoses;
        public SoundEffect leon;

        public SoundManager()
        {
            playerShootSound = null;
            explodeSound = null;
            gameMusic = null;
            gunsNRoses = null;
            bombSound = null;
            missileLaunchSound = null;
            leon = null;
 
        }

        public void LoadContent(ContentManager Content)
        {
            playerShootSound = Content.Load<SoundEffect>("gunshot");
            explodeSound = Content.Load<SoundEffect>("explode");
            gameMusic = Content.Load<Song>("CCR");
            gunsNRoses = Content.Load<Song>("GNR");
            bombSound = Content.Load<SoundEffect>("bombdrop");
            missileLaunchSound = Content.Load<SoundEffect>("missilelaunch");
            leon = Content.Load<SoundEffect>("leon");

        }
    }
}
