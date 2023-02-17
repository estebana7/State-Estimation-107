import matplotlib.pyplot as plt
import numpy as np
import createNetc1 as cnc1
import createNetc2 as cnc2
import createNetc3 as cnc3
import estimateNetc1 as se1
import estimateNetc2 as se2
import estimateNetc3 as se3

#%% Fluxo de Potência

tensaoRealc1 = cnc1.netc1.res_bus.vm_pu
anguloRealc1 = cnc1.netc1.res_bus.va_degree

tensaoRealc2 = cnc2.netc2.res_bus.vm_pu
anguloRealc2 = cnc2.netc2.res_bus.va_degree

tensaoRealc3 = cnc3.netc3.res_bus.vm_pu
anguloRealc3 = cnc3.netc3.res_bus.va_degree

#%% Estimação de Estados

#printar a estimação
tensaoEstimadac1 = se1.cnc1.netc1.res_bus_est.vm_pu #magnitude estimada
anguloEstimadoc1 = se1.cnc1.netc1.res_bus_est.va_degree #fase estimada

tensaoEstimadac2 = se2.cnc2.netc2.res_bus_est.vm_pu #magnitude estimada
anguloEstimadoc2 = se2.cnc2.netc2.res_bus_est.va_degree #fase estimada

tensaoEstimadac3 = se3.cnc3.netc3.res_bus_est.vm_pu #magnitude estimada
anguloEstimadoc3 = se3.cnc3.netc3.res_bus_est.va_degree #fase estimada

#Erros de estimação
erroEstimacaoTensaoc1 = abs((tensaoEstimadac1 - tensaoRealc1)/tensaoRealc1)*100
erroEstimacaoAngularc1 = abs((anguloEstimadoc1 - anguloRealc1)/anguloRealc1)*100

erroEstimacaoTensaoc2 = abs((tensaoEstimadac2 - tensaoRealc2)/tensaoRealc2)*100
erroEstimacaoAngularc2 = abs((anguloEstimadoc2 - anguloRealc2)/anguloRealc2)*100

erroEstimacaoTensaoc3 = abs((tensaoEstimadac3 - tensaoRealc3)/tensaoRealc3)*100
erroEstimacaoAngularc3 = abs((anguloEstimadoc3 - anguloRealc3)/anguloRealc3)*100

#Média dos erros de estimação
mediaErroc1 = sum(erroEstimacaoTensaoc1)/len(erroEstimacaoTensaoc1)
max_erroEstimacaoTensaoc1 = max(erroEstimacaoTensaoc1)
index_erroEstimcaoTensaoc1 = list(erroEstimacaoTensaoc1).index(max(erroEstimacaoTensaoc1))

print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc1, 3))
print("O maior erro percentual de tensão é:", '\n', round(max_erroEstimacaoTensaoc1, 3))
print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimcaoTensaoc1, '\n')

mediaErroc2 = sum(erroEstimacaoTensaoc2)/len(erroEstimacaoTensaoc2)
max_erroEstimacaoTensaoc2 = max(erroEstimacaoTensaoc2)
index_erroEstimcaoTensaoc2 = list(erroEstimacaoTensaoc2).index(max(erroEstimacaoTensaoc2))

print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc2, 3))
print("O maior erro percentual de tensão é:", '\n', round(max_erroEstimacaoTensaoc2, 3))
print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimcaoTensaoc2, '\n')

mediaErroc3 = sum(erroEstimacaoTensaoc3)/len(erroEstimacaoTensaoc3)
max_erroEstimacaoTensaoc3 = max(erroEstimacaoTensaoc3)
index_erroEstimcaoTensaoc3 = list(erroEstimacaoTensaoc3).index(max(erroEstimacaoTensaoc3))

print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc3, 3))
print("O maior erro percentual de tensão é:", '\n', round(max_erroEstimacaoTensaoc3, 3))
print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimcaoTensaoc3, '\n')

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

y1Realc1 = tensaoRealc1

y2Estimadoc1 = tensaoEstimadac1
y2Estimadoc2 = tensaoEstimadac2
y2Estimadoc3 = tensaoEstimadac3

x_pos = np.arange(len(barrax))

#========================================================================================

fig = plt.figure()
ax = plt.subplot(111)

plt.plot(x_pos, y1Realc1, label = "Real", linestyle="-", color='#5979f2')
plt.plot(x_pos, y2Estimadoc1, label = "SCADA", linestyle="-", color='#ec622a')
plt.plot(x_pos, y2Estimadoc2, label = "SCADA sem redundância", linestyle="-", color='#50b580')
plt.plot(x_pos, y2Estimadoc3, label = "SCADA com redundância", linestyle="-", color='#5b00c2')
plt.xlabel('Barras do Sistema')
plt.ylabel('Tensão (p.u)')
lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
text = ax.text(-0.2,1.05, "", transform=ax.transAxes)
plt.savefig("VBarras.pdf", bbox_extra_artists=(lgd, text), bbox_inches='tight')
plt.show()

#========================================================================================

y3Erroc1 = erroEstimacaoTensaoc1
y3Erroc2 = erroEstimacaoTensaoc2
y3Erroc3 = erroEstimacaoTensaoc3

fig = plt.figure()
ax = plt.subplot(111)

plt.plot(x_pos, y3Erroc1, label = "Erros SCADA (%)", linestyle="-", color='#ec622a')
plt.plot(x_pos, y3Erroc2, label = "Erros SCADA sem redundância (%)", linestyle="-", color='#50b580')
plt.plot(x_pos, y3Erroc3, label = "Erros SCADA com redundância (%)", linestyle="-", color='#5b00c2')
plt.xlabel('Barras do Sistema')
plt.ylabel('Erros de Estimação de Tensão (%)')
lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
text = ax.text(-0.2,1.05, "", transform=ax.transAxes)
plt.savefig("ErrosBarrasV.pdf", bbox_extra_artists=(lgd, text), bbox_inches='tight')
plt.show()

#========================================================================================

# y4Realc1 = anguloRealc1
# y5Estimadoc1 = anguloEstimadoc1

# plt.plot(x_pos, y4Realc1, label = "Real", linestyle="-", color='#5979f2')
# plt.plot(x_pos, y5Estimadoc1, label = "Estimado", linestyle="-", color='#50b580')
# plt.xlabel('Barras do Sistema')
# plt.ylabel('Ângulo (graus)')
# plt.legend()
# plt.savefig("ThetaBarras.pdf")
# plt.show()

#========================================================================================

# y6Erroc1 = erroEstimacaoAngularc1

# plt.plot(x_pos, y6Erroc1, label = "Erros de Estimação Angular (%)", linestyle="-", color='#50b580')
# plt.xlabel('Barras do Sistema')
# plt.ylabel('Erros de Estimação Angular (%)')
# plt.legend()
# plt.savefig("ErrosBarrasA.pdf")
# plt.show()

