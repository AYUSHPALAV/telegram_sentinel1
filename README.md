Project Setup Steps:

1.Create Project Directory

bashCopymkdir telegram-sentinel
cd telegram-sentinel

3.Create project structure
mkdir telegram_sentinel
touch telegram_sentinel/__init__.py
touch telegram_sentinel/main.py
touch telegram_sentinel/nlp_engine.py
touch telegram_sentinel/ml_classifier.py
touch telegram_sentinel/alert_system.py
touch telegram_sentinel/telegram_api.py
touch train_model.py
touch requirements.txt
touch README.md

3.Set Up Virtual Environment
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

4.Install Required Dependencies
pip install asyncio scikit-learn pandas numpy transformers torch python-telegram-bot joblib
pip freeze > requirements.txt


5.Train the Model
Open a terminal in VS Code and run:
python train_model.py

6.Run the Telegram Sentinel
In the VS Code terminal:python -m telegram_sentinel.main
