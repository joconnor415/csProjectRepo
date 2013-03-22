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
    public class TankEnemy
    {
        public Rectangle enemCollRect;
        public Texture2D enemTexture, enemBullTexture;
        public Vector2 enemPosition;
        public int enemHealth, enemSpeed, enemBullDelay, enemToughness;
        public bool isVisible;
        public List<Projectile> enemBullList;

        public TankEnemy(Texture2D newTexture, Vector2 newPosition, Texture2D newBulletTexture)
        {
            enemBullList = new List<Projectile>();
            enemTexture = newTexture;
            enemBullTexture = newBulletTexture;
            enemHealth = 5;
            enemPosition = newPosition;
            enemToughness = 1;
            enemBullDelay = 100;
            enemSpeed = 5;
            isVisible = true;
        }
        public void Update(GameTime gameTime)
        {
            //Update collision rect
            enemCollRect = new Rectangle((int)enemPosition.X, (int)enemPosition.Y, enemTexture.Width, enemTexture.Height);

            //Update Enemy postion
            enemPosition.Y += enemSpeed;


            if (enemPosition.Y >= 720)
                enemPosition.Y = -75;
            EnemyShoot();
            UpdateProjectiles();
        }
        public void Draw(SpriteBatch spriteBatch)
        {
            //draw enemy
            spriteBatch.Draw(enemTexture, enemPosition, Color.White);

            //draw enemy projectile
            foreach (Projectile b in enemBullList)
            {
                b.Draw(spriteBatch);
            }
        }
        public void UpdateProjectiles()
        {

            foreach (Projectile b in enemBullList)
            {
                //collision rect for projectiles
                b.projectileRectangle = new Rectangle((int)b.projectilePosition.X, (int)b.projectilePosition.Y, b.projectileTexture.Width, b.projectileTexture.Height);

                b.projectilePosition.Y = b.projectilePosition.Y + b.projectileSpeed;
                if (b.projectilePosition.Y >= 720)
                    b.onScreen = false;
            }

            //go thru bullet list and remove all bullets that aren't visible
            for (int i = 0; i < enemBullList.Count; i++)
            {
                if (!enemBullList[i].onScreen)
                {
                    enemBullList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void EnemyShoot()
        {
            //shoot only if bull delay resets
            if (enemBullDelay >= 0)
                enemBullDelay--;

            if (enemBullDelay <= 0)
            {
                //create bullet for enemy, at center of texture
                Projectile newBullet = new Projectile(enemBullTexture);
                newBullet.projectilePosition = new Vector2(enemPosition.X + enemTexture.Width / 2 - newBullet.projectileTexture.Width / 2, enemPosition.Y + enemTexture.Height);

                newBullet.onScreen = true;

                if (enemBullList.Count() < 20)
                    enemBullList.Add(newBullet);
            }
            if (enemBullDelay == 100)
                enemBullDelay = 100;

        }
    }

}
