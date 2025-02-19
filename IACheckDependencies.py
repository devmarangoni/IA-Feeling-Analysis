import sys
import subprocess

def check():
    libraries = {
        "scikit-learn": "sklearn",
        "NLTK": "nltk",
        "Joblib": "joblib",
        "Deep Translator": "deep_translator"
    }

    missing = []

    for lib_name, import_name in libraries.items():
        try:
            lib = __import__(import_name)
            print(f"✅ {lib_name} instalado - versão: {lib.__version__}")
        except ImportError:
            print(f"❌ {lib_name} não encontrado.")
            missing.append(lib_name)

    if missing:
        print("\n⚠️ Algumas bibliotecas estão faltando:", ", ".join(missing))
        choice = input("Deseja instalar automaticamente? (s/n): ").strip().lower()

        if choice == "s":
            for lib in missing:
                print(f"📦 Instalando {lib}...")
                subprocess.run([sys.executable, "-m", "pip", "install", lib.replace(' ', '-').lower()], check=True)
            
            print("\n✅ Todas as dependências foram instaladas com sucesso!")
            print("Reinicie o programa para aplicar as mudanças.\n")
            sys.exit(0)
        else:
            print("\n⚠️ Instalação cancelada. Instale manualmente usando:")
            print(f"\n  pip install {' '.join(lib.replace(' ', '-').lower() for lib in missing)}\n")
            sys.exit(1)