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
    class Player
    {
        public Texture2D playerTexture, playerHealthTexture;
        public Vector2 position, playerHealthPos;
        public int playerSpeed, playerHealth;
        public Rectangle playerCollRect, playerHealthRect;
        public Vector2 playerOrigin;
        float rotation;

        public Texture2D playerBullTexture;
        public Texture2D playerBombTexture;
        public Texture2D playerMissileTexture;
        public float playerBullDelay;
        public float playerBombDelay;
        public float playerMissileDelay;
        public bool isColl;
        public List<Projectile> playerBullList;
        public List<Bomb> playerBombList;
        public List<Missile> playerMissileList;
        SoundManager sm = new SoundManager();
        public Color[] textureData;

        //Player Constructor
        public Player()
        {
            playerTexture = null;
            position = new Vector2(600, 550);
            playerSpeed = 10;
            isColl = false;
            playerBullList = new List<Projectile>();
            playerBombList = new List<Bomb>();
            playerMissileList = new List<Missile>();
            playerBullDelay = 5;
            playerBombDelay = 20;
            playerMissileDelay = 20;
            playerHealth = 400;
            playerHealthPos = new Vector2(50, 50);
        }

        public void LoadContent(ContentManager Content)
        {
            playerTexture = Content.Load<Texture2D>("playerplane");
            playerBullTexture = Content.Load<Texture2D>("playerbullet");
            playerHealthTexture = Content.Load<Texture2D>("health");
            playerBombTexture = Content.Load<Texture2D>("bombscaled");
            playerMissileTexture = Content.Load<Texture2D>("missile");
            sm.LoadContent(Content);
            textureData = new Color[playerTexture.Width * playerTexture.Height];
            playerTexture.GetData(textureData);
        }

        public void Draw(SpriteBatch spriteBatch)
        {
            //spriteBatch.Draw(playerTexture, position, Color.White);
            spriteBatch.Draw(playerHealthTexture, playerHealthRect, Color.White);
            spriteBatch.Draw(playerTexture, position, null, Color.White, rotation, playerOrigin, 1f, SpriteEffects.None, 0);
            foreach (Projectile b in playerBullList)
                b.Draw(spriteBatch);
            foreach (Bomb bomb in playerBombList)
                bomb.Draw(spriteBatch);
            foreach (Missile missile in playerMissileList)
                missile.Draw(spriteBatch);
        }

        public void Update(GameTime gameTime)
        {
            GamePadState player1 = GamePad.GetState(PlayerIndex.One);
            if (player1.DPad.Up == ButtonState.Pressed)
                position.Y = position.Y - playerSpeed;
            if (player1.DPad.Down == ButtonState.Pressed)
                position.Y = position.Y + playerSpeed;
            if (player1.DPad.Left == ButtonState.Pressed)
                position.X = position.X - playerSpeed;
            if (player1.DPad.Right == ButtonState.Pressed)
                position.X = position.X + playerSpeed;
            if (player1.Buttons.A == ButtonState.Pressed)
            {
                ShootProjectiles();
            }
            UpdateProjectiles();
            if (player1.Buttons.B == ButtonState.Pressed)
            {
                DropBomb();
            }
            UpdateBombs();
            if (player1.Buttons.X == ButtonState.Pressed)
            {
                fireMissiles();
            }
            UpdateMissiles();

            KeyboardState keystate = Keyboard.GetState();
            //Collision Rectangle for player
            playerCollRect = new Rectangle((int)position.X, (int)position.Y, playerTexture.Width, playerTexture.Height);
            playerHealthRect= new Rectangle((int)playerHealthPos.X, (int)playerHealthPos.Y, playerHealth, playerHealthTexture.Height);
            //Player Plane Controls
            if (keystate.IsKeyDown(Keys.Up))
                position.Y = position.Y - playerSpeed;
            if (keystate.IsKeyDown(Keys.Down))
                position.Y = position.Y + playerSpeed;
            if (keystate.IsKeyDown(Keys.Left))
                position.X = position.X - playerSpeed;
            if (keystate.IsKeyDown(Keys.Right))
                position.X = position.X + playerSpeed;
            if (keystate.IsKeyDown(Keys.Space))
            {
                ShootProjectiles();
            }
            UpdateProjectiles();
            if (keystate.IsKeyDown(Keys.LeftShift))
            {
                DropBomb();
            }
            UpdateBombs();
            if (keystate.IsKeyDown(Keys.CapsLock))
            {
                fireMissiles();
            }
            UpdateMissiles();

            playerOrigin = new Vector2(playerCollRect.Width / 2, playerCollRect.Height / 2);
            if (position.X <= 0)
                position.X = 0;
            if (position.X >= 1280 - playerTexture.Width)
                position.X = 1280 - playerTexture.Width;
            if (position.Y <= 0)
                position.Y = 0;
            if (position.Y >= 720 - playerTexture.Height)
                position.Y = 720 - playerTexture.Height;
        }
        

        public void ShootProjectiles()
        {
            //shoot if delay resets
            if (playerBullDelay >= 0)
                playerBullDelay--;

            //if bulletdelay at 0; create new bullet at player position, show on screen and add it to the bullet list
            if (playerBullDelay <= 0)
            {
                sm.playerShootSound.Play();
                Projectile newBullet = new Projectile(playerBullTexture);
                Projectile newBullet1 = new Projectile(playerBullTexture);
                newBullet.projectilePosition = new Vector2(position.X + 45 - newBullet.projectileTexture.Width / 2, position.Y -45);
                newBullet1.projectilePosition = new Vector2(position.X - 45 - newBullet.projectileTexture.Width / 2, position.Y -45);
                newBullet.onScreen = true;
                newBullet1.onScreen = true;


                if (playerBullList.Count() < 40)
                    playerBullList.Add(newBullet);
                    playerBullList.Add(newBullet1);
                    
            }
            //reset bullet delay
            if (playerBullDelay == 0)
                playerBullDelay = 5;
        }

        public void DropBomb()
        {
            //shoot if delay resets
            if (playerBombDelay >= 0)
                playerBombDelay--;

            //if bulletdelay at 0; create new bullet at player position, show on screen and add it to the bullet list
            if (playerBombDelay <= 0)
            {
                sm.bombSound.Play();
                Bomb newBomb = new Bomb(playerBombTexture);
                newBomb.bombPosition = new Vector2(position.X + 45 - newBomb.bombTexture.Width / 2, position.Y - 45);
                newBomb.onScreen = true;


                if (playerBombList.Count() < 40)
                    playerBombList.Add(newBomb);
                playerBombList.Add(newBomb);

            }
            //reset bullet delay
            if (playerBombDelay == 0)
                playerBombDelay = 20;
        }

        public void fireMissiles()
        {
            //shoot if delay resets
            if (playerMissileDelay >= 0)
                playerMissileDelay--;

            //if bulletdelay at 0; create new bullet at player position, show on screen and add it to the bullet list
            if (playerMissileDelay <= 0)
            {
                sm.missileLaunchSound.Play();
                Missile newMissile = new Missile(playerMissileTexture);
                newMissile.missilePosition = new Vector2(position.X + 45 - newMissile.missileTexture.Width / 2, position.Y - 45);
                newMissile.onScreen = true;

                if (playerMissileList.Count() < 40)
                    playerMissileList.Add(newMissile);
                playerMissileList.Add(newMissile);

            }
            //reset bullet delay
            if (playerMissileDelay == 0)
                playerMissileDelay = 20;
        }
        public void UpdateProjectiles()
        {
            //for each bullet in bulletList, when bullet hits end of screen remove from list
            foreach (Projectile b in playerBullList)
            {
                //collsion rectangle for bullets in bullet list
                b.projectileRectangle = new Rectangle((int)b.projectilePosition.X, (int)b.projectilePosition.Y, b.projectileTexture.Width, b.projectileTexture.Height);

                b.projectilePosition.Y = b.projectilePosition.Y - b.projectileSpeed;
                if (b.projectilePosition.Y <= 0)
                    b.onScreen = false;
            }

            //go thru bullet list, remove bullets not on screen
            for (int i = 0; i < playerBullList.Count; i++)
            {
                if (!playerBullList[i].onScreen)
                {
                    playerBullList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void UpdateBombs()
        {
            //for each bullet in bulletList, when bullet hits end of screen remove from list
            foreach (Bomb bomb in playerBombList)
            {
                //collsion rectangle for bullets in bullet list
                bomb.bombRectangle = new Rectangle((int)bomb.bombPosition.X, (int)bomb.bombPosition.Y, bomb.bombTexture.Width, bomb.bombTexture.Height);

                bomb.bombPosition.Y = bomb.bombPosition.Y - bomb.bombSpeed;
                if (bomb.bombPosition.Y <= 0)
                    bomb.onScreen = false;
            }

            //go thru bullet list, remove bullets not on screen
            for (int i = 0; i < playerBombList.Count; i++)
            {
                if (!playerBombList[i].onScreen)
                {
                    playerBombList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void UpdateMissiles()
        {
            //for each bullet in bulletList, when bullet hits end of screen remove from list
            foreach (Missile missile in playerMissileList)
            {
                //collsion rectangle for bullets in bullet list
                missile.missileRectangle = new Rectangle((int)missile.missilePosition.X, (int)missile.missilePosition.Y, missile.missileTexture.Width, missile.missileTexture.Height);

                missile.missilePosition.Y = missile.missilePosition.Y - missile.missileSpeed;
                if (missile.missilePosition.Y <= 0)
                    missile.onScreen = false;
            }

            //go thru bullet list, remove bullets not on screen
            for (int i = 0; i < playerMissileList.Count; i++)
            {
                if (!playerMissileList[i].onScreen)
                {
                    playerMissileList.RemoveAt(i);
                    i--;
                }
            }
        }
    }

}

