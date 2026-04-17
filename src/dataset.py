import tensorflow as tf


def check_gpu():
    
    gpus = tf.config.list_physical_devices("GPU")
    
    if gpus:
        print(f"✅ SUCCÈS : {len(gpus)} GPU(s) détecté(s) par TensorFlow !")
        for i, gpu in enumerate(gpus):
            print(f"   -> Détails GPU {i} : {gpu}")
            
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            print("✅ Option 'Memory Growth' (croissance de la mémoire) activée avec succès.")
        except RuntimeError as e:
            print(f"❌ Erreur lors de la configuration de la mémoire : {e}")
    else:
        print("⚠️ ATTENTION : Aucun GPU détecté. TensorFlow utilisera le CPU de ton ordinateur.")

