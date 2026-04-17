# 👁️ SleepGuard-AI : Détection de Somnolence par IA

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)

## 📖 À propos du projet
Ce projet implémente une intelligence artificielle capable de détecter l'endormissement en temps réel à l'aide d'une webcam. Conçu pour prévenir les risques liés à la somnolence (comme au volant), le système repose sur un Réseau de Neurones Convolutifs (CNN) entraîné de zéro (from scratch) pour analyser l'ouverture et la fermeture des yeux.

## ✨ Fonctionnalités
- **Entraînement Local sur GPU :** Modèle CNN personnalisé et optimisé avec TensorFlow/Keras.
- **Inférence en Temps Réel :** Analyse du flux vidéo de la webcam via OpenCV et MediaPipe.
- **Système d'Alerte :** Déclenchement d'une alarme si les yeux restent fermés au-delà d'un seuil critique.
- **Intégration Continue (CI) :** Pipeline GitHub Actions pour vérifier la compilation de l'architecture du modèle à chaque push.

## 🛠️ Structure du Projet
- `src/model.py` : Architecture du réseau de neurones.
- `src/train.py` : Script d'entraînement du modèle (nécessite une carte graphique).
- `src/detect.py` : Script principal pour lancer la détection en temps réel sur la webcam.

## 🚀 Installation & Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/ton-pseudo/SleepGuard-AI.git](https://github.com/ton-pseudo/SleepGuard-AI.git)
   cd SleepGuard-AI