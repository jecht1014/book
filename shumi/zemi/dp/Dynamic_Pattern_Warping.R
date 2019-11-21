library("ramify")

#input:�p�^�[���̒���n,�ꎟ���p�^�[���̍\���v�fV
#output:�����_���Ȑ���1:length(V)�ŕ\�����p�^�[��a
#�ꎟ���p�^�[���̍\���v�fV�̗v�f����p���Đ���1����length(V)�܂ł̐�����
#������n+1�������V���ȃp�^�[����Ԃ��֐�
ranP <- function(n, V) {
  x <- 1/length(V)
  a <- runif(n+1)
  for(i in 1:length(V)) {
    for(j in 1:(n+1)) {
      if(a[j] < x){
        a[j] <- i
      }
    }
    x <- x+1/length(V)
  }

#  for(i in 1:(n+1)) {
#    a[i] <- V[a[i]]
#  }
  return(a)
}

#input:�����ɕύX�����p�^�[��a, �ꎟ���p�^�[���̗v�f�̏W��V
#output:�ꎟ���p�^�[���̗v�f�ō��ꂽ�p�^�[��b
#ranP�ō��ꂽ�����̈ꎟ���p�^�[����V�̈ꎟ���p�^�[���ɕϊ����Ԃ��֐�
pback <- function(a, V) {
  for(i in 1:length(a))
    a[i] <- V[a[i]]
  return(a)
}

#input
I <- 10 #�p�^�[��A�̒���
J <- 10 #�p�^�[��B�̒���
V <- c(0,1) #�ꎟ���p�^�[���̗v�f�̏W��
alpha <- rbind(c(0,1),c(1,0)) #V�̗ގ��x
A <- ranP(I, V)
B <- ranP(J, V)

#begin
#�����l�ݒ�
g <- matrix(-1, nrow = I+1, ncol = J+1) #g�̏�����
g[1,1] <- alpha[A[1],B[1]]
for(j in 2:(J+1))
  g[1,j] <- 10000

#�œK�L�k�֐�w�̏��
h <- matrix(-1, nrow = I+1, ncol = J+1)

#D(A,B)�̌v�Z
for(i in 2:(I+1)) {
  for(j in 1:(J+1)) {
    #�ŏ��l�T���͈͂̏ꍇ����
    if(j == 1) {
      g[i, j] <- alpha[A[i], B[j]] + g[i-1, j]
      h[i, j] <- j
    } else if(j == 2) {
      g[i, j] <- alpha[A[i], B[j]] + min(g[i-1, c(j-1, j)])
      h[i, j] <- argmin(rbind(g[i-1, c(j-1, j)]), rows = TRUE) + j - 2
    } else {
      g[i, j] <- alpha[A[i], B[j]] + min(g[i-1, c(j-2, j-1, j)])
      h[i, j] <- argmin(rbind(g[i-1, c(j-2, j-1, j)]), rows = TRUE) + j - 3
    }
  }
}
D <- g[I+1, J+1]

#�œK�L�k�֐��̌���
w <- numeric(I+1)
w[I+1] <- J+1
for(i in (I+1):2)
  w[i-1] <- h[i, w[i]]
w <- w-1

A <- pback(A, V)
B <- pback(B, V)

A
B
w