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
    class Explosion
    {
        public Texture2D texture;
        public Vector2 position;
        public float timer;
        public float interval;
        public Vector2 origin;
        public int currentframe;
        public int spriteWidth;
        public int spriteHeight;
        public Rectangle sourceRect;
        public bool isVisible;

        public Explosion(Texture2D newTexture, Vector2 newPosition)
        {
            position = newPosition;
            texture = newTexture;
            timer = 0f;
            interval = 60f;
            currentframe = 1;
            spriteWidth = 128;
            spriteHeight = 128;
            isVisible = true;
        }

        public void LoadContent(ContentManager Content)
        {

        }

        public void Update (GameTime gameTime)
        {
            //Increase Timer by number of millisec since update was last called
            timer+=(float) gameTime.ElapsedGameTime.TotalMilliseconds;

            //Check timer is more than the chosen interval
            if (timer > interval)
            {
                //show next frame;
                currentframe++;
                //reset timer
                timer=0f;
            }
            //if were on the last frame, make explosion invisible, reset currentframe to beginning of spritesheet 
            if (currentframe==17)
            {
                isVisible = false;
                currentframe=0;
            }
            sourceRect= new Rectangle(currentframe* spriteWidth, 0, spriteWidth, spriteHeight);
            origin = new Vector2(sourceRect.Width / 2, sourceRect.Height / 2);   
        }
        public void Draw(SpriteBatch spriteBatch)
        {
            //if visible then draw
            if (isVisible == true)
                spriteBatch.Draw(texture, position, sourceRect, Color.White, 0f, origin, 1.0f, SpriteEffects.None, 0);
        }
    }
}
