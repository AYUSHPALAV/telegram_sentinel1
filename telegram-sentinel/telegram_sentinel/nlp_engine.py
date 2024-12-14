import re
import numpy as np
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class ThreatSignature:
    pattern: str
    risk_score: float
    category: str

class AdvancedNLPEngine:
    def __init__(self):
        self.threat_signatures = self._load_threat_signatures()
    
    def _load_threat_signatures(self) -> List[ThreatSignature]:
        return [
            ThreatSignature(
                pattern=r'\b(guaranteed\s+return|free\s+money)',
                risk_score=0.8,
                category='financial_fraud'
            ),
            ThreatSignature(
                pattern=r'\b(crypto\s+scam|pump\s+and\s+dump)',
                risk_score=0.9,
                category='investment_scam'
            )
        ]
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """Perform comprehensive text analysis"""
        return {
            'text_length': len(text),
            'word_count': len(text.split()),
            'detected_threats': self._detect_threats(text),
            'complexity_score': self._calculate_complexity(text)
        }
    
    def _detect_threats(self, text: str) -> List[Dict]:
        """Detect potential threats based on predefined signatures"""
        threats = []
        for signature in self.threat_signatures:
            if re.search(signature.pattern, text, re.IGNORECASE):
                threats.append({
                    'pattern': signature.pattern,
                    'risk_score': signature.risk_score,
                    'category': signature.category
                })
        return threats
    
    def _calculate_complexity(self, text: str) -> float:
        """Calculate text complexity"""
        words = text.split()
        unique_words = len(set(words))
        return (unique_words / len(words)) * np.log(len(words) + 1)