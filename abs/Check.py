from subprocess import check_output, CalledProcessError
from sys import stdin, stderr, argv

try:
    inp = open("solution.txt", 'r')
    check_output([argv[1]], stdin=inp)

except CalledProcessError as err:
    print(err.output, file=stderr)
    print("\nJob succeed", file=stderr)
except:
    print("Something went wrong...")
    raise
else:
    print("Not crushed")
finally:
    inp.close()
