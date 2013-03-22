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
    public class FirstAid
    {
        public Rectangle aidCollRect;
        public Texture2D aidTexture, enemBullTexture;
        public Vector2 aidPosition;
        public int aidSpeed;
        public bool isVisible;
        

        public FirstAid(Texture2D newTexture, Vector2 newPosition)
        {
            
            aidTexture = newTexture;
     
            aidPosition = newPosition;
            aidSpeed = 5;
            isVisible = true;
        }
        public void Update(GameTime gameTime)
        {
            //Update collision rect
            aidCollRect = new Rectangle((int)aidPosition.X, (int)aidPosition.Y, aidTexture.Width, aidTexture.Height);

            //Update Enemy postion
            aidPosition.Y += aidSpeed;


            if (aidPosition.Y >= 720)
                aidPosition.Y = -75;
        }
        public void Draw(SpriteBatch spriteBatch)
        {
            //draw enemy
            spriteBatch.Draw(aidTexture, aidPosition, Color.White);

        }
       
    }

}
