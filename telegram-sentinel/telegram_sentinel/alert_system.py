import pandas as pd
from datetime import datetime

class AlertSystem:
    def __init__(self):
        self.alerts = []
        self.threat_history = pd.DataFrame(columns=[
            'timestamp', 'channel', 'user', 'risk_score', 'threat_categories'
        ])
    
    def create_alert(self, message, risk_score, nlp_result):
        """Create and log comprehensive alert"""
        alert = {
            'timestamp': datetime.now(),
            'message': message.text,
            'user': message.user.username,
            'channel': message.channel.name,
            'risk_score': risk_score,
            'threat_categories': [
                threat['category'] for threat in nlp_result['detected_threats']
            ]
        }
        
        self.alerts.append(alert)
        self._update_threat_history(alert)
        return alert
    
    def _update_threat_history(self, alert):
        """Update comprehensive threat tracking database"""
        new_entry = pd.DataFrame([{
            'timestamp': alert['timestamp'],
            'channel': alert['channel'],
            'user': alert['user'],
            'risk_score': alert['risk_score'],
            'threat_categories': ','.join(alert['threat_categories'])
        }])
        
        self.threat_history = pd.concat([self.threat_history, new_entry], ignore_index=True)