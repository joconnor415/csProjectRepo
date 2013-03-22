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
    public class Projectile
    {
        public Rectangle projectileRectangle;
        public Texture2D projectileTexture;
        public Vector2 projectileOrigin;
        public Vector2 projectilePosition;
        public bool onScreen;
        public float projectileSpeed;

        //Projectile constructor
        public Projectile(Texture2D newTexture)
        {
            projectileSpeed = 10;
            projectileTexture = newTexture;
            onScreen = false;
        }

        //Draw Projectile
        public void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(projectileTexture, projectilePosition, Color.White);
        }
    }
}
