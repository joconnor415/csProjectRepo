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
    public class Missile
    {
        public Rectangle missileRectangle;
        public Texture2D missileTexture;
        public Vector2 missileOrigin;
        public Vector2 missilePosition;
        public bool onScreen;
        public float missileSpeed;

        //Projectile constructor
        public Missile(Texture2D newTexture)
        {
            missileSpeed = 7;
            missileTexture = newTexture;
            onScreen = false;
        }

        //Draw Projectile
        public void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(missileTexture, missilePosition, Color.White);
        }
    }
}
