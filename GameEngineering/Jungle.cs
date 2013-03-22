using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Content;

namespace FinalShooter
{
    public class Jungle
    {
        public Texture2D jungleTexture;
        public Vector2 junglePos1;
        public Vector2 junglePos2;
        public int jungleSpeed;

        public Jungle()
        {
            jungleTexture = null;
            junglePos1 = new Vector2(0, 0);
            junglePos2 = new Vector2(0, -720);
            jungleSpeed = 5;
        }

        public void LoadContent(ContentManager Content)
        {
            jungleTexture = Content.Load<Texture2D>("back1");
        }

        public void Draw(SpriteBatch spritebatch)
        {
            spritebatch.Draw(jungleTexture, junglePos1, Color.White);
            spritebatch.Draw(jungleTexture, junglePos2, Color.White);
        }

        public void Update(GameTime gametime)
        {
            junglePos1.Y = junglePos1.Y + jungleSpeed;
            junglePos2.Y = junglePos2.Y + jungleSpeed;
            if (junglePos1.Y >= 720)
            {
                junglePos1.Y = 0;
                junglePos2.Y = -720;
            }
        }
    }
}
