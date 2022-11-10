import scipy.integrate
import numpy
import matplotlib.pyplot as pyplot
from matplotlib import pyplot as plt


def SIR_model(y, t, beta, gamma):

    S, I, R = y

    dS_dt = -beta*S*I

    dI_dt = beta*S*I - gamma*I
    dR_dt = gamma*I

    return ([dS_dt, dI_dt, dR_dt])


print("안녕 나는 SMC야. SIR 모델로 감염병 종식을 예측해줄게.")
str = input()
if str != '응':
    print("프로그램을 종료합니다.")
    quit()


print("취약자는 몇명인가요?")
S0 = input()
print("최초감염자는 몇명인가요?")
I0 = input()
print("회복자는 몇명인가요")
R0 = input()
allPlus = int(S0) + int(I0) + int(R0)

S0 = int(S0)/allPlus * 100
I0 = int(I0)/allPlus * 100
R0 = int(R0)/allPlus * 100

beta = 0.35
gamma = 0.1

print("그래프를 그려드렸어요! 앞으로도 자주 이용해주세요!")

t = numpy.linspace(0, 100, 10000)
solution = scipy.integrate.odeint(
    SIR_model, [S0, I0, R0], t, args=(beta, gamma))
solution = numpy.array(solution)


plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.show()

print("프로그램을 종료합니다.")
quit()
