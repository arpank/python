from numpy import loadtxt, where, reshape, transpose, log, e, zeros, array, ones, append
from pylab import scatter, show, legend, xlabel, ylabel
def sigmoid(X):
    '''Compute the sigmoid function '''
    #d = zeros(shape=(X.shape))

    den = 1.0 + e ** (-1.0 * X)

    d = 1.0 / den

    return d
def cost_function_reg(theta, X, y, l):
    '''Compute the cost and partial derivatives as grads
    '''

    h = sigmoid(X.dot(theta))

    thetaR = theta[1:, 0]

    J = (1.0 / m) * ((-y.T.dot(log(h))) - ((1 - y.T).dot(log(1.0 - h)))) \
            + (l / (2.0 * m)) * (thetaR.T.dot(thetaR))

    delta = h - y
    sumdelta = delta.T.dot(X[:, 1])
    grad1 = (1.0 / m) * sumdelta

    XR = X[:, 1:X.shape[1]]
    sumdelta = delta.T.dot(XR)

    grad = (1.0 / m) * (sumdelta + l * thetaR)

    out = zeros(shape=(grad.shape[0], grad.shape[1] + 1))

    out[:, 0] = grad1
    out[:, 1:] = grad

    return J.flatten(), out.T.flatten()

def map_feature(x1, x2):
    '''
    Maps the two input features to quadratic features.

    Returns a new feature array with more features, comprising of
    X1, X2, X1 ** 2, X2 ** 2, X1*X2, X1*X2 ** 2, etc...

    Inputs X1, X2 must be the same size
    '''
    x1.shape = (x1.size, 1)
    x2.shape = (x2.size, 1)
    degree = 6
    out = ones(shape=(x1[:, 0].size, 1))

    m, n = out.shape

    for i in range(1, degree + 1):
        for j in range(i + 1):
            r = (x1 ** (i - j)) * (x2 ** j)
            out = append(out, r, axis=1)
            print("First number is {i} and number is {j} out is {out}".format(i=i, j=j, out=out) )
    return out

#load the dataset
data = loadtxt('ex2data2.txt', delimiter=',')
X = data[:, 0:2]
y = data[:, 2]

pos = where(y == 1)
neg = where(y == 0)
scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
scatter(X[neg, 0], X[neg, 1], marker='x', c='r')
xlabel('Microchip Test 1')
ylabel('Microchip Test 2')
legend(['y = 1', 'y = 0'])
show()

m, n = X.shape

m, n = X.shape

y.shape = (m, 1)

it = map_feature(X[:, 0], X[:, 1])

#Initialize theta parameters
initial_theta = zeros(shape=(it.shape[1], 1))

#Set regularization parameter lambda to 1
l = 1

# Compute and display initial cost and gradient for regularized logistic
# regression
#cost, grad = cost_function_reg(initial_theta, it, y, l)

#def decorated_cost(theta):
   # return cost_function_reg(theta, it, y, l)

#Set regularization parameter lambda to 1
l = 1

# Compute and display initial cost and gradient for regularized logistic
# regression
cost, grad = cost_function_reg(initial_theta, it, y, l)

#print fmin_bfgs(decorated_cost, initial_theta, maxfun=400)

def decorated_cost(theta):
    return cost_function_reg(theta, it, y, l)