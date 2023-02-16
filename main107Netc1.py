import pandapower as pp
from pandapower.estimation import estimate
import matplotlib.pyplot as plt
import numpy as np
import createNetc1 as cnc1
import estimateNetc1 as se1

#%% Fluxo de Potência

#print(cnc1.netc1.res_bus) #Print da resposta das barras
#print(netc1.netc1.res_line) #Print da resposta das linhas

tensaoReal = cnc1.netc1.res_bus.vm_pu
anguloReal = cnc1.netc1.res_bus.va_degree

#%% Estimação de Estados

#printar a estimação
tensaoEstimada = se1.cnc1.netc1.res_bus_est.vm_pu #magnitude estimada
anguloEstimado = se1.cnc1.netc1.res_bus_est.va_degree #fase estimada

#print("Valores de magnitude estimados:",'\n', tensaoEstimada, '\n')
#print("Valores de ângulo estimados:",'\n', anguloEstimado, '\n')

erroEstimacaoTensao = abs((tensaoEstimada - tensaoReal)/tensaoReal)*100
erroEstimacaoAngular = abs((anguloEstimado - anguloReal)/anguloReal)*100
#print("O erro percentual de estimação da tensão, por barra, é:", '\n', erroEstimacaoTensao, '\n')

mediaErro = sum(erroEstimacaoTensao)/len(erroEstimacaoTensao)
max_erroEstimacaoTensao = max(erroEstimacaoTensao)
index_erroEstimcaoTensao = list(erroEstimacaoTensao).index(max(erroEstimacaoTensao))

print("A média dos erros percentuais de tensão é:", '\n', round(mediaErro, 3))
print("O maior erro percentual de tensão é:", '\n', round(max_erroEstimacaoTensao, 3))
print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimcaoTensao, '\n')

#%% Gráficos

barrax = [cnc1.b1, cnc1.b2, cnc1.b3, cnc1.b4, cnc1.b5, 
          cnc1.b6, cnc1.b7, cnc1.b8, cnc1.b9, cnc1.b10, 
          cnc1.b11, cnc1.b12, cnc1.b13, cnc1.b14, cnc1.b15, 
          cnc1.b16, cnc1.b17, cnc1.b18, cnc1.b19, cnc1.b20, 
          cnc1.b21, cnc1.b22, cnc1.b23, cnc1.b24, cnc1.b25, 
          cnc1.b26, cnc1.b27, cnc1.b28, cnc1.b29, cnc1.b30, 
          cnc1.b31, cnc1.b32, cnc1.b33, cnc1.b34, cnc1.b35, 
          cnc1.b36, cnc1.b37, cnc1.b38, cnc1.b39, cnc1.b40, 
          cnc1.b41, cnc1.b42, cnc1.b43, cnc1.b44, cnc1.b45, 
          cnc1.b46, cnc1.b47, cnc1.b48, cnc1.b49, cnc1.b50, 
          cnc1.b51, cnc1.b52, cnc1.b53, cnc1.b54, cnc1.b55, 
          cnc1.b56, cnc1.b57, cnc1.b58, cnc1.b59, cnc1.b60, 
          cnc1.b61, cnc1.b62, cnc1.b63, cnc1.b64, cnc1.b65, 
          cnc1.b66, cnc1.b67, cnc1.b68, cnc1.b69, cnc1.b70, 
          cnc1.b71, cnc1.b72, cnc1.b73, cnc1.b74, cnc1.b75, 
          cnc1.b76, cnc1.b77, cnc1.b78, cnc1.b79, cnc1.b80, 
          cnc1.b81, cnc1.b82, cnc1.b83, cnc1.b84, cnc1.b85, 
          cnc1.b86, cnc1.b87, cnc1.b88, cnc1.b89, cnc1.b90, 
          cnc1.b91, cnc1.b92, cnc1.b93, cnc1.b94, cnc1.b95, 
          cnc1.b96, cnc1.b97, cnc1.b98, cnc1.b99, cnc1.b100, 
          cnc1.b101, cnc1.b102, cnc1.b103, cnc1.b104, cnc1.b105, 
          cnc1.b106, cnc1.b107]

y1Real = tensaoReal
y2Estimado = tensaoEstimada #trocar por tensaoEstimada quando funcionar

x_pos = np.arange(len(barrax))

#========================================================================================

plt.plot(x_pos, y1Real, label = "Real", linestyle="-", color='#5979f2')
plt.plot(x_pos, y2Estimado, label = "Estimada", linestyle="-", color='#ec622a')
plt.xlabel('Barras do Sistema')
plt.ylabel('Tensão (p.u)')
plt.legend()
plt.savefig("SCADA_VBarras.pdf")
plt.show()

#========================================================================================

y3Erro = erroEstimacaoTensao
plt.plot(x_pos, y3Erro, label = "Erros de Estimação de Tensão (%)", linestyle="-", color='#ec622a')
plt.xlabel('Barras do Sistema')
plt.ylabel('Erros de Estimação de Tensão (%)')
plt.legend()
plt.savefig("SCADA_ErrosBarrasV.pdf")
plt.show()

#========================================================================================

y4Real = anguloReal
y5Estimado = anguloEstimado

plt.plot(x_pos, y4Real, label = "Real", linestyle="-", color='#5979f2')
plt.plot(x_pos, y5Estimado, label = "Estimado", linestyle="-", color='#ec622a')
plt.xlabel('Barras do Sistema')
plt.ylabel('Ângulo (graus)')
plt.legend()
plt.savefig("SCADA_ThetaBarras.pdf")
plt.show()

#========================================================================================

y6Erro = erroEstimacaoAngular
plt.plot(x_pos, y6Erro, label = "Erros de Estimação Angular (%)", linestyle="-", color='#ec622a')
plt.xlabel('Barras do Sistema')
plt.ylabel('Erros de Estimação Angular (%)')
plt.legend()
plt.savefig("SCADA_ErrosBarrasA.pdf")
plt.show()

