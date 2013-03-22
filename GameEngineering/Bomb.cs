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
    public class Bomb
    {
        public Rectangle bombRectangle;
        public Texture2D bombTexture;
        public Vector2 bombOrigin;
        public Vector2 bombPosition;
        public bool onScreen;
        public float bombSpeed;

        //Projectile constructor
        public Bomb(Texture2D newTexture)
        {
            bombSpeed = 3;
            bombTexture = newTexture;
            onScreen = false;
        }

        //Draw Projectile
        public void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(bombTexture, bombPosition, Color.White);
        }
    }
}
