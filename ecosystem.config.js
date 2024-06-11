module.exports = {
  apps: [
    {
      name: "check-and-restart",
      script: "./check_and_restart.py",
      interpreter: "python3",
      cron_restart: "*/15 * * * *", // Runs every 15 minutes
      watch: false,
      autorestart: false,
    },
  ],
};
