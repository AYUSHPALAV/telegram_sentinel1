import asyncio
import logging
from .telegram_api import TelegramAPISimulator, Channel, User
from .nlp_engine import AdvancedNLPEngine
from .ml_classifier import AdvancedMLClassifier
from .alert_system import AlertSystem

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('TelegramSentinel')

class TelegramSentinel:
    def __init__(self):
        self.telegram_api = TelegramAPISimulator()
        self.nlp_engine = AdvancedNLPEngine()
        self.ml_classifier = AdvancedMLClassifier()
        self.alert_system = AlertSystem()
        
        # Try to load pre-trained model
        if not self.ml_classifier.load_model():
            logger.warning("No pre-trained model found. Please run train_model.py first.")
            raise RuntimeError("Model not trained. Run train_model.py to train the model.")
    
    async def monitor_channel(self, channel):
        """Monitor a specific Telegram channel"""
        while True:
            try:
                messages = await self.telegram_api.get_new_messages(channel)
                for message in messages:
                    await self.process_message(message)
                await asyncio.sleep(5)  # Polling interval
            except Exception as e:
                logger.error(f"Channel monitoring error: {e}")
                await asyncio.sleep(5)  # Prevent rapid error logging
    
    async def process_message(self, message):
        """Process and analyze each message"""
        try:
            # Perform NLP analysis
            nlp_result = self.nlp_engine.analyze(message.text)
            
            # Classify message risk
            risk_score = self.ml_classifier.classify(message, nlp_result)
            
            # Log the analysis
            logger.info(f"Message from {message.user.username}: Risk Score = {risk_score}")
            
            # Create alert for high-risk messages
            if risk_score > 0.7:
                alert = self.alert_system.create_alert(message, risk_score, nlp_result)
                self._handle_high_risk_alert(alert)
        
        except Exception as e:
            logger.error(f"Error processing message: {e}")
    
    def _handle_high_risk_alert(self, alert):
        """Handle high-risk alerts"""
        logger.warning(f"High-Risk Alert Detected: {alert}")
        # You could add additional alert handling here, 
        # such as sending notifications, logging to a file, etc.

async def main():
    try:
        sentinel = TelegramSentinel()
        
        # Monitor multiple channels
        channels = [
            Channel("CryptoScams"),
            Channel("InvestmentOpportunities")
        ]
        
        # Run channel monitoring concurrently
        await asyncio.gather(
            *[sentinel.monitor_channel(channel) for channel in channels]
        )
    
    except Exception as e:
        logger.error(f"Critical error in main application: {e}")
        # Optionally, add more robust error handling or recovery mechanisms

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application terminated by user.")
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")