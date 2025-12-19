import argparse
from src.assistant import Assistant


def main():
    parser = argparse.ArgumentParser(description='CLI para el asistente virtual')
    parser.add_argument('text', nargs='?', help='Texto a procesar por el asistente')
    args = parser.parse_args()

    a = Assistant()
    a.load_skills_from_package('src.skills')

    if args.text:
        print(a.handle(args.text))
        return

    try:
        while True:
            text = input('>> ')
            if text.strip().lower() in ('exit', 'quit'):
                break
            print(a.handle(text))
    except (KeyboardInterrupt, EOFError):
        print('\nSaliendo...')


if __name__ == '__main__':
    main()
