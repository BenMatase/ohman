import subprocess
import man_parser as parser

def main():
    result = subprocess.check_output(['man', 'man'])
    parser.parse(result)

if __name__ == '__main__':
    main()
