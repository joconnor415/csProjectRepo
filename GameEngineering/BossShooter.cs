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
    public class BossShooter
    {
        public Rectangle bossCollRect;
        public Texture2D bossTexture, bossBullTexture, bossMissTexture;
        public Vector2 bossPosition;
        public int bossHealth, bossSpeed, bossBullDelay, bossToughness;
        public bool isVisible;
        public List<Projectile> bossBullList;
        public List<Missile> bossMissList;
        public int bossMissDelay;

        public BossShooter(Texture2D newTexture, Vector2 newPosition, Texture2D newBulletTexture, Texture2D newMissTexture)
        {
            bossBullList = new List<Projectile>();
            bossMissList = new List<Missile>();
            bossTexture = newTexture;
            bossBullTexture = newBulletTexture;
            bossMissTexture = newMissTexture;
            bossHealth = 30000;
            bossPosition = newPosition;
            bossToughness = 1;
            bossBullDelay = 100;
            bossSpeed = 5;
            isVisible = true;
        }
        public void Update(GameTime gameTime)
        {
            //Update collision rect
            bossCollRect = new Rectangle((int)bossPosition.X, (int)bossPosition.Y, bossTexture.Width, bossTexture.Height);
            bossPosition.X += bossSpeed;
            if (bossPosition.X > 1500  ||
                bossPosition.X < -400)
                bossSpeed *= -1;

            EnemyShoot();
            EnemyShootMissiles();
            UpdateMissiles();
            UpdateProjectiles();
        }
        public void Draw(SpriteBatch spriteBatch)
        {
            //draw enemy
            spriteBatch.Draw(bossTexture, bossPosition, Color.White);

            //draw enemy projectile
            foreach (Projectile b in bossBullList)
            {
                b.Draw(spriteBatch);
            }
            foreach (Missile m in bossMissList)
            {
                m.Draw(spriteBatch);
            }
        }
        public void UpdateProjectiles()
        {

            foreach (Projectile b in bossBullList)
            {
                //collision rect for projectiles
                b.projectileRectangle = new Rectangle((int)b.projectilePosition.X, (int)b.projectilePosition.Y, b.projectileTexture.Width, b.projectileTexture.Height);

                b.projectilePosition.Y = b.projectilePosition.Y + b.projectileSpeed;
                if (b.projectilePosition.Y >= 720)
                    b.onScreen = false;
            }

            //go thru bullet list and remove all bullets that aren't visible
            for (int i = 0; i < bossBullList.Count; i++)
            {
                if (!bossBullList[i].onScreen)
                {
                    bossBullList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void UpdateMissiles()
        {

            foreach (Missile m in bossMissList)
            {
                //collision rect for projectiles
                m.missileRectangle = new Rectangle((int)m.missilePosition.X, (int)m.missilePosition.Y, m.missileTexture.Width, m.missileTexture.Height);

                m.missilePosition.Y = m.missilePosition.Y + m.missileSpeed;
                if (m.missilePosition.Y >= 720)
                    m.onScreen = false;
            }

            //go thru bullet list and remove all bullets that aren't visible
            for (int i = 0; i < bossMissList.Count; i++)
            {
                if (!bossMissList[i].onScreen)
                {
                    bossMissList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void EnemyShoot()
        {
            //shoot only if bull delay resets
            if (bossBullDelay >= 0)
                bossBullDelay--;

            if (bossBullDelay <= 0)
            {
                //create bullet for enemy, at center of texture
                Projectile newBullet = new Projectile(bossBullTexture);
                newBullet.projectilePosition = new Vector2(bossPosition.X + bossTexture.Width / 2 - newBullet.projectileTexture.Width / 2, bossPosition.Y + bossTexture.Height);

                newBullet.onScreen = true;

                if (bossBullList.Count() < 20)
                    bossBullList.Add(newBullet);
            }
            if (bossBullDelay == 100)
                bossBullDelay = 100;

        }
        public void EnemyShootMissiles()
        {
            //shoot only if bull delay resets
            if (bossMissDelay >= 0)
                bossMissDelay--;

            if (bossMissDelay <= 0)
            {
                //create bullet for enemy, at center of texture
                Missile newMiss = new Missile(bossMissTexture);
                newMiss.missilePosition = new Vector2(bossPosition.X + bossTexture.Width / 2 - newMiss.missileTexture.Width / 2, bossPosition.Y + bossTexture.Height);

                newMiss.onScreen = true;

                if (bossHealth <= 20000 && bossMissList.Count < 1)
                {
                    bossMissList.Add(newMiss);
                }
            }
            if (bossBullDelay == 1000)
                bossBullDelay = 1000;

        }
    }

}
