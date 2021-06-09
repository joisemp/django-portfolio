This project requires mongodb to run locally by default to activate the mongodb in linux use : sudo systemctl start mongod
If it fails run this command and try the above command again : sudo systemctl daemon-reload
Verify that mongodb has started successfully : sudo systemctl status mongod
Stop mongodb : sudo systemctl stop mongod
Restart mongodb : sudo systemctl restart mongod