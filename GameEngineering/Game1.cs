using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace FinalShooter
{

    public class Game1 : Microsoft.Xna.Framework.Game
    {
        public enum State
        {
            Menu,
            Playing,
            gameOver
        }
        private const int BackBufferWidth = 1280;
        private const int BackBufferHeight = 720;

        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        Random random = new Random();
        public int enemyBulletDamage;

        Player player = new Player();
        Jungle background = new Jungle();

        List<Enemy> enemyList = new List<Enemy>();
        List<TankEnemy> tankEnemyList = new List<TankEnemy>();
        List<Explosion> explosionList = new List<Explosion>();
        List<Boss> bossList = new List<Boss>();
        List<BossShooter> bossShooterList = new List<BossShooter>();
        List<Missile> missileList = new List<Missile>();
        List<FirstAid> firstAidList = new List<FirstAid>();
        Display display = new Display();
        SoundManager sm = new SoundManager();
        public Texture2D menuPic;
        public Texture2D gameOverPic;
        State gameState = State.Menu;
        WinBackground win = new WinBackground();

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            graphics.PreferredBackBufferHeight = BackBufferHeight;
            graphics.PreferredBackBufferWidth = BackBufferWidth;
            Content.RootDirectory = "Content";
            enemyBulletDamage = 2;
            menuPic = null;
            gameOverPic = null;
        }

        protected override void Initialize()
        {
            base.Initialize();
        }

        protected override void LoadContent()
        {
            spriteBatch = new SpriteBatch(GraphicsDevice);
            background.LoadContent(Content);
            player.LoadContent(Content);
            display.LoadContent(Content);
            sm.LoadContent(Content);
            menuPic = Content.Load<Texture2D>("Menu");
            MediaPlayer.Play(sm.gunsNRoses);
            gameOverPic = Content.Load<Texture2D>("gameover");
        }


        protected override void UnloadContent()
        {

        }


        protected override void Update(GameTime gameTime)
        {

            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
                this.Exit();

            switch (gameState)
            {

                case State.Playing:
                    {

                        background.jungleSpeed = 5;
                        foreach (TankEnemy te in tankEnemyList)
                        {
                            if (te.enemCollRect.Intersects(player.playerCollRect))
                            {
                                if (PixelCollision(player.playerTexture, te.enemTexture, player.playerCollRect, te.enemCollRect))
                                {
                                    player.playerHealth -= 30;
                                    te.isVisible = false;
                                }


                            }

                            for (int i = 0; i < te.enemBullList.Count; i++)
                            {
                                if (player.playerCollRect.Intersects(te.enemBullList[i].projectileRectangle))
                                {
                                    if (PixelCollision(player.playerTexture, te.enemBullList[i].projectileTexture, player.playerCollRect, te.enemBullList[i].projectileRectangle))
                                    {
                                        player.playerHealth -= enemyBulletDamage;
                                        te.enemBullList[i].onScreen = false;
                                    }

                                }
                            }

                            for (int i = 0; i < player.playerBullList.Count; i++)
                            {
                                if (player.playerBullList[i].projectileRectangle.Intersects(te.enemCollRect))
                                {
                                    if (PixelCollision(player.playerBullList[i].projectileTexture, te.enemTexture, player.playerBullList[i].projectileRectangle, te.enemCollRect))
                                    {
                                        //destroy player bull and enemy 
                                        sm.explodeSound.Play();
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(te.enemPosition.X, te.enemPosition.Y)));
                                        display.playerScore += 50;
                                        player.playerBullList[i].onScreen = false;
                                        te.isVisible = false;
                                    }
                                }
                            }
                            for (int i = 0; i < player.playerBombList.Count; i++)
                            {
                                if (player.playerBombList[i].bombRectangle.Intersects(te.enemCollRect))
                                {
                                    if (PixelCollision(player.playerBombList[i].bombTexture, te.enemTexture, player.playerBombList[i].bombRectangle, te.enemCollRect))
                                    {
                                        //destroy player bull and enemy 
                                        sm.explodeSound.Play();
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(te.enemPosition.X, te.enemPosition.Y)));
                                        display.playerScore += 100;
                                        player.playerBombList[i].onScreen = false;
                                        te.isVisible = false;
                                    }
                                }
                            }
                            te.Update(gameTime);
                        }
                        foreach (FirstAid fa in firstAidList)
                        {
                            if (fa.aidCollRect.Intersects(player.playerCollRect))
                            {
                                if (PixelCollision(player.playerTexture, fa.aidTexture, player.playerCollRect, fa.aidCollRect))
                                {
                                    player.playerHealth += 100;
                                    fa.isVisible = false;
                                }

                            }

                            fa.Update(gameTime);
                        }
                        foreach (Enemy e in enemyList)
                        {

                            if (e.enemCollRect.Intersects(player.playerCollRect))
                            {
                                if (PixelCollision(player.playerTexture, e.enemTexture, player.playerCollRect, e.enemCollRect))
                                {
                                    player.playerHealth -= 30;
                                    e.isVisible = false;
                                }

                            }

                            for (int i = 0; i < e.enemBullList.Count; i++)
                            {
                                if (player.playerCollRect.Intersects(e.enemBullList[i].projectileRectangle))
                                {
                                    if (PixelCollision(player.playerTexture, e.enemBullList[i].projectileTexture, player.playerCollRect, e.enemBullList[i].projectileRectangle))
                                    {
                                        player.playerHealth -= enemyBulletDamage;
                                        e.enemBullList[i].onScreen = false;
                                    }
                                }
                            }

                            for (int i = 0; i < player.playerBullList.Count; i++)
                            {
                                if (player.playerBullList[i].projectileRectangle.Intersects(e.enemCollRect))
                                {
                                    //destroy player bull and enemy 
                                    if (PixelCollision(player.playerBullList[i].projectileTexture, e.enemTexture, player.playerBullList[i].projectileRectangle, e.enemCollRect))
                                    {
                                        sm.explodeSound.Play();
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(e.enemPosition.X, e.enemPosition.Y)));
                                        display.playerScore += 50;
                                        player.playerBullList[i].onScreen = false;
                                        e.isVisible = false;
                                    }
                                }
                            }
                            for (int i = 0; i < player.playerMissileList.Count; i++)
                            {
                                Vector2 enemyPos = e.enemPosition;

                                if (e.enemPosition.X < player.playerMissileList[i].missilePosition.X)
                                    player.playerMissileList[i].missilePosition.X -= e.enemSpeed;
                                else if (e.enemPosition.X > player.playerMissileList[i].missilePosition.X)
                                    player.playerMissileList[i].missilePosition.X += e.enemSpeed;

                                if (e.enemPosition.Y < player.playerMissileList[i].missilePosition.Y)
                                    player.playerMissileList[i].missilePosition.Y -= e.enemSpeed;
                                else if (e.enemPosition.Y > player.playerMissileList[i].missilePosition.Y)
                                    player.playerMissileList[i].missilePosition.Y += e.enemSpeed;


                                if (player.playerMissileList[i].missileRectangle.Intersects(e.enemCollRect))
                                {

                                    //destroy player bull and enemy 
                                    if (PixelCollision(player.playerMissileList[i].missileTexture, e.enemTexture, player.playerMissileList[i].missileRectangle, e.enemCollRect))
                                    {
                                        sm.explodeSound.Play();
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(e.enemPosition.X, e.enemPosition.Y)));
                                        display.playerScore += 50;
                                        player.playerMissileList[i].onScreen = false;
                                        e.isVisible = false;
                                    }
                                }
                            }
                            e.Update(gameTime);
                        }
                        foreach (BossShooter bs in bossShooterList)
                        {
                            //Vector2 enemyPos = e.enemPosition;

                            if (bs.bossCollRect.Intersects(player.playerCollRect))
                            {
                                if (PixelCollision(player.playerTexture, bs.bossTexture, player.playerCollRect, bs.bossCollRect))
                                {
                                    player.playerHealth -= 30;
                                    bs.isVisible = false;
                                }

                            }
                            //if (e.enemCollRect.Intersects(player.playerCollRect))
                            //{
                            //    player.playerHealth -= 30;
                            //    e.isVisible = false;
                            //}


                            for (int i = 0; i < bs.bossBullList.Count; i++)
                            {
                                if (player.playerCollRect.Intersects(bs.bossBullList[i].projectileRectangle))
                                {
                                    if (PixelCollision(player.playerTexture, bs.bossBullList[i].projectileTexture, player.playerCollRect, bs.bossBullList[i].projectileRectangle))
                                    {
                                        player.playerHealth -= enemyBulletDamage;
                                        bs.bossBullList[i].onScreen = false;
                                    }
                                }
                            }

                            for (int i = 0; i < bs.bossMissList.Count; i++)
                            {

                                if (player.position.X < bs.bossMissList[i].missilePosition.X)
                                    bs.bossMissList[i].missilePosition.X -= player.playerSpeed;
                                else if (player.position.X > bs.bossMissList[i].missilePosition.X)
                                    bs.bossMissList[i].missilePosition.X += player.playerSpeed;

                                if (player.position.Y < bs.bossMissList[i].missilePosition.Y)
                                    bs.bossMissList[i].missilePosition.Y -= player.playerSpeed;
                                else if (player.position.Y > bs.bossMissList[i].missilePosition.Y)
                                    bs.bossMissList[i].missilePosition.Y += player.playerSpeed;

                                if (player.playerCollRect.Intersects(bs.bossMissList[i].missileRectangle))
                                {
                                    if (PixelCollision(player.playerTexture, bs.bossMissList[i].missileTexture, player.playerCollRect, bs.bossMissList[i].missileRectangle))
                                    {
                                        player.playerHealth -= enemyBulletDamage;
                                        bs.bossMissList[i].onScreen = false;
                                    }
                                }
                            }


                            for (int i = 0; i < player.playerBullList.Count; i++)
                            {
                                if (player.playerBullList[i].projectileRectangle.Intersects(bs.bossCollRect))
                                {
                                    //destroy player bull and enemy 
                                    if (PixelCollision(player.playerBullList[i].projectileTexture, bs.bossTexture, player.playerBullList[i].projectileRectangle, bs.bossCollRect))
                                    {
                                        sm.explodeSound.Play();
                                        bs.bossHealth -= 50;
                                        if (bs.bossHealth <= 2000)
                                        {
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2 + 40, bs.bossPosition.Y + bs.bossTexture.Height / 2 + 30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2 - 30, bs.bossPosition.Y + bs.bossTexture.Height / 2 - 30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2 + 30, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2 - 30, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2 + 30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2 - 30)));
                                            //bs.isVisible = false;
                                            display.playerScore += 50;
                                        }
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                        player.playerBullList[i].onScreen = false;
                                        bs.bossHealth -= 50;
                                    }
                                }
                            }
                            for (int i = 0; i < player.playerMissileList.Count; i++)
                            {
                                Vector2 enemyPos = bs.bossPosition;

                                if (bs.bossPosition.X +bs.bossTexture.Width/2 < player.playerMissileList[i].missilePosition.X)
                                    player.playerMissileList[i].missilePosition.X -= Math.Abs(bs.bossSpeed);
                                else if (bs.bossPosition.X+bs.bossTexture.Width / 2 > player.playerMissileList[i].missilePosition.X)
                                    player.playerMissileList[i].missilePosition.X += Math.Abs(bs.bossSpeed);

                                if (bs.bossPosition.Y + bs.bossTexture.Height / 2 < player.playerMissileList[i].missilePosition.Y)
                                    player.playerMissileList[i].missilePosition.Y -= bs.bossSpeed;
                                else if (bs.bossPosition.Y + bs.bossTexture.Height / 2 > player.playerMissileList[i].missilePosition.Y)
                                    player.playerMissileList[i].missilePosition.Y += bs.bossSpeed;


                                if (player.playerMissileList[i].missileRectangle.Intersects(bs.bossCollRect))
                                {

                                    //destroy player bull and enemy 
                                    if (PixelCollision(player.playerMissileList[i].missileTexture, bs.bossTexture, player.playerMissileList[i].missileRectangle, bs.bossCollRect))
                                    {
                                        sm.explodeSound.Play();
                                        bs.bossHealth -= 50;
                                        if (bs.bossHealth <= 2000)
                                        {
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2+40, bs.bossPosition.Y + bs.bossTexture.Height / 2+30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2-30, bs.bossPosition.Y + bs.bossTexture.Height / 2-30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2+30, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2-30, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2+30)));
                                            explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2-30)));
                                            //bs.isVisible = false;
                                            display.playerScore += 50;
                                        }
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(bs.bossPosition.X + bs.bossTexture.Width / 2, bs.bossPosition.Y + bs.bossTexture.Height / 2)));
                                        player.playerMissileList[i].onScreen = false;
                                        bs.bossHealth -= 50;
                                    }
                                }
                            }
                            bs.Update(gameTime);
                        }

                        foreach (Boss boss in bossList)
                        {
                            Vector2 playPos = player.position;

                            if (player.position.X < boss.enemPosition.X)
                                boss.enemPosition.X -= player.playerSpeed;
                            else if (player.position.X > boss.enemPosition.X)
                                boss.enemPosition.X += player.playerSpeed;

                            if (player.position.Y < boss.enemPosition.Y)
                                boss.enemPosition.Y -= player.playerSpeed;
                            else if (player.position.Y > boss.enemPosition.Y)
                                boss.enemPosition.Y += player.playerSpeed;

                            if (boss.enemCollRect.Intersects(player.playerCollRect))
                            {
                                if (PixelCollision(player.playerTexture, boss.enemTexture, player.playerCollRect, boss.enemCollRect))
                                {
                                    player.playerHealth -= 30;
                                    boss.isVisible = false;
                                }

                            }
                            //if (e.enemCollRect.Intersects(player.playerCollRect))
                            //{
                            //    player.playerHealth -= 30;
                            //    e.isVisible = false;
                            //}


                            for (int i = 0; i < boss.enemBullList.Count; i++)
                            {
                                if (player.playerCollRect.Intersects(boss.enemBullList[i].projectileRectangle))
                                {
                                    if (PixelCollision(player.playerTexture, boss.enemBullList[i].projectileTexture, player.playerCollRect, boss.enemBullList[i].projectileRectangle))
                                    {
                                        player.playerHealth -= enemyBulletDamage;
                                        boss.enemBullList[i].onScreen = false;
                                    }
                                }
                            }

                            for (int i = 0; i < player.playerBullList.Count; i++)
                            {
                                if (player.playerBullList[i].projectileRectangle.Intersects(boss.enemCollRect))
                                {
                                    //destroy player bull and enemy 
                                    if (PixelCollision(player.playerBullList[i].projectileTexture, boss.enemTexture, player.playerBullList[i].projectileRectangle, boss.enemCollRect))
                                    {
                                        sm.explodeSound.Play();
                                        explosionList.Add(new Explosion(Content.Load<Texture2D>("explosion3"), new Vector2(boss.enemPosition.X, boss.enemPosition.Y)));
                                        display.playerScore += 50;
                                        player.playerBullList[i].onScreen = false;
                                        boss.isVisible = false;
                                    }
                                }
                            }
                            boss.Update(gameTime);
                        }
                        foreach (Explosion ex in explosionList)
                        {
                            ex.Update(gameTime);
                        }

                        //if player health hits 0 go to game over state
                        if (player.playerHealth <= 0)
                            gameState = State.gameOver;
                        
                        player.Update(gameTime);
                        background.Update(gameTime);
                        manageExplosions();
                        //display.Update(gameTime);
                        LoadTankEnemies();
                        LoadEnemies();
                        LoadFirstAid();
                        //LoadBossShooter();
                        if (display.playerScore >= 1000)
                        {
                            enemyList.Clear();
                            //tankEnemyList.Clear();
                            LoadBoss();
                            //LoadBossShooter();
                            display.Update(gameTime);
                            if (display.playerScore >= 2000)
                            {
                                tankEnemyList.Clear();
                                bossList.Clear();
                                //bossShooterList.Clear();
                                LoadBossShooter();
                                if (bossShooterList.ElementAt(0).bossHealth <= 0)
                                {
                                    display.playerScore = 100000;
                                    bossShooterList.Clear();
                                    firstAidList.Clear();
                                    gameState = State.gameOver;

                                    break;
                                }
                  
                            }
                            break;
                         
                        }
                        display.Update(gameTime);
                        break;
                    }
                case State.Menu:
                    {

                        GamePadState player1 = GamePad.GetState(PlayerIndex.One);
                        if (player1.Buttons.B == ButtonState.Pressed)
                        {
                            gameState = State.Playing;
                            sm.leon.Play();
                            MediaPlayer.Play(sm.gameMusic);
                        }

                        KeyboardState keyState = Keyboard.GetState();
                        if (keyState.IsKeyDown(Keys.Enter))
                        {
                            gameState = State.Playing;
                            sm.leon.Play();
                            MediaPlayer.Play(sm.gameMusic);
                        }
                        background.Update(gameTime);
                        background.jungleSpeed = 1;
                        break;
                    }
                case State.gameOver:
                    {
                        //Get Keyboard State
                        KeyboardState keyState = Keyboard.GetState();
                        GamePadState player1 = GamePad.GetState(PlayerIndex.One);

                        if (player1.Buttons.B == ButtonState.Pressed)
                        {
                            enemyList.Clear();
                            firstAidList.Clear();
                            tankEnemyList.Clear();
                            bossList.Clear();
                            bossShooterList.Clear();
                            explosionList.Clear();
                            player.playerHealth = 200;
                            display.playerScore = 0;
                            gameState = State.Menu;
                        }

                        if (keyState.IsKeyDown(Keys.Escape))
                        {
                            enemyList.Clear();
                            firstAidList.Clear();
                            tankEnemyList.Clear();
                            bossList.Clear();
                            bossShooterList.Clear();
                            explosionList.Clear();
                            player.playerHealth = 200;
                            display.playerScore = 0;
                            gameState = State.Menu;
                        }

                        //Stop Music
                        MediaPlayer.Stop();


                        break;
                    }
            }

            base.Update(gameTime);
        }

        private bool PixelCollision(Texture2D playerText, Texture2D enemText, Rectangle player, Rectangle enemy)
        {
            Color[] colorData1 = new Color[playerText.Width * playerText.Height];
            Color[] colorData2 = new Color[enemText.Width * enemText.Height];
            playerText.GetData<Color>(colorData1);
            enemText.GetData<Color>(colorData2);

            int top, bottom, left, right;

            top = Math.Max(player.Top, enemy.Top);
            bottom = Math.Min(player.Bottom, enemy.Bottom);
            left = Math.Max(player.Left, enemy.Left);
            right = Math.Min(player.Right, enemy.Right);

            for (int y = top; y < bottom; y++)
            {
                for (int x = left; x < right; x++)
                {
                    Color A = colorData1[(y - player.Top) * player.Width + (x - player.Left)];
                    Color B = colorData2[(y - enemy.Top) * (enemy.Width) + (x - enemy.Left)];

                    if (A.A != 0 && B.A != 0)
                        return true;
                }
            }
            return false;
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.Black);
            spriteBatch.Begin();
            switch (gameState)
            {
                case State.Playing:
                    {
                        background.Draw(spriteBatch);
                        player.Draw(spriteBatch);

                        foreach (TankEnemy te in tankEnemyList)
                        {
                            te.Draw(spriteBatch);
                        }
                        foreach (Enemy e in enemyList)
                        {
                            e.Draw(spriteBatch);
                        }
                        foreach (Boss boss in bossList)
                        {
                            boss.Draw(spriteBatch);
                        }
                        foreach (BossShooter bs in bossShooterList)
                        {
                            bs.Draw(spriteBatch);
                        }
                        foreach (FirstAid fa in firstAidList)
                        {
                            fa.Draw(spriteBatch);
                        }
                        foreach (Explosion ex in explosionList)
                        {
                            ex.Draw(spriteBatch);
                        }
                        player.Draw(spriteBatch);
                        display.Draw(spriteBatch);
                        break;
                    }
                case State.Menu:
                    {
                        background.Draw(spriteBatch);
                        spriteBatch.Draw(menuPic, new Vector2(0, 0), Color.White);
                        break;
                    }
                case State.gameOver:
                    {
                        spriteBatch.Draw(gameOverPic, new Vector2(0, 0), Color.White);
                        if (display.playerScore >= 100000)
                        {
                            spriteBatch.DrawString(display.playerScoreFont, "Congrats You Won!", new Vector2(600, 30), Color.Red);
                            spriteBatch.DrawString(display.playerScoreFont, "You are the Jungle Shooter!", new Vector2(600, 50), Color.Red);
                        }

                        spriteBatch.DrawString(display.playerScoreFont, "Your Final Score was: " + display.playerScore.ToString(), new Vector2(600, 350), Color.Red);
                        break;
                    }
            }


            spriteBatch.End();
            base.Draw(gameTime);
        }

        public void LoadEnemies()
        {

            int randY = random.Next(-600, -50);
            int randX = random.Next(0, 1240);
            if (enemyList.Count() < 3)
            {
                enemyList.Add(new Enemy(Content.Load<Texture2D>("enemyplane3"), new Vector2(randX, randY), Content.Load<Texture2D>("computerbullet")));
            }


            for (int i = 0; i < enemyList.Count; i++)
            {
                if (!enemyList[i].isVisible)
                {
                    enemyList.RemoveAt(i);
                    i--;
                }
            }
        }

        public void LoadBoss()
        {

            int randY = random.Next(-600, -50);
            int randX = random.Next(0, 1240);
            if (bossList.Count() < 3)
            {
                bossList.Add(new Boss(Content.Load<Texture2D>("enemyplane3"), new Vector2(randX, randY), Content.Load<Texture2D>("computerbullet")));
            }


            for (int i = 0; i < bossList.Count; i++)
            {
                if (!bossList[i].isVisible)
                {
                    bossList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void LoadBossShooter()
        {

            int randY = random.Next(0, 200);
            int randX = random.Next(-300, -200);
            if (bossShooterList.Count() < 1)
            {
                bossShooterList.Add(new BossShooter(Content.Load<Texture2D>("bossplane"), new Vector2(randX, randY), Content.Load<Texture2D>("computerbullet"), Content.Load<Texture2D>("bossmissile")));
            }


            for (int i = 0; i < bossShooterList.Count; i++)
            {
                if (!bossShooterList[i].isVisible)
                {
                    bossShooterList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void LoadFirstAid()
        {
            int randY = random.Next(-100, -50);
            int randX = random.Next(0, 1240);
            if (player.playerHealth <=50)
            {
                if (firstAidList.Count() < 1)
                {
                    firstAidList.Add(new FirstAid(Content.Load<Texture2D>("firstaid"), new Vector2(randX, randY)));
                }
            }

            for (int i = 0; i < firstAidList.Count; i++)
            {
                if (!firstAidList[i].isVisible)
                {
                    firstAidList.RemoveAt(i);
                    i--;
                }
            }
        }

        public void LoadTankEnemies()
        {

            int randY = random.Next(-1000, -100);
            int randX = random.Next(300, 600);
            if (tankEnemyList.Count() < 3)
            {
                tankEnemyList.Add(new TankEnemy(Content.Load<Texture2D>("enemytank"), new Vector2(randX, randY), Content.Load<Texture2D>("computerbullet")));
            }


            for (int i = 0; i < tankEnemyList.Count; i++)
            {
                if (!tankEnemyList[i].isVisible)
                {
                    tankEnemyList.RemoveAt(i);
                    i--;
                }
            }
        }
        public void manageExplosions()
        {
            for (int i = 0; i < explosionList.Count; i++)
            {
                if (!explosionList[i].isVisible)
                {
                    explosionList.RemoveAt(i);
                    i--;
                }
            }
        }

    }
}
