from game import RippleEffect
from solver import RippleEffectSolver


def main():
    user_groups = [[(1,0),(0,0),(0,1),(0,2)],
                [(0,3),(1,3)],
                [(0,4)],
                [(1,1),(1,2),(2,2)],
                [(2,0),(2,1)],
                [(2,3),(1,4),(2,4),(3,4)],
                [(3,0),(3,1),(3,2),(4,0),(4,1)],
                [(3,3)],
                [(4,2)],
                [(4,3),(4,4)]]

    print("Board: ")
    ripple = RippleEffect(5, user_groups)

    l = [(0, 0, 2), (1)]
    ripple.insert(0, 0, 2)
    ripple.insert(1, 4, 3)
    ripple.insert(3, 1, 4)
    ripple.insert(4, 0, 1)
    print(ripple)
    print('-----------------------------')
    solver = RippleEffectSolver(ripple)
    solver.solve()

    print(ripple)



if __name__ == "__main__":
    main()
