import matplotlib.pyplot as plt
import createNetc1 as cnc1
import estimateNetc1 as se1
import estimateNetc2 as se2
import estimateNetc3 as se3
import general as g
import numpy as np

#%% Gráficos e prints

if g.N == 1:

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
    
    y1Realc1 = g.tensaoRealc1
    
    y2Estimadoc1 = se1.tensaoEstimadac1
    y2Estimadoc2 = se2.tensaoEstimadac2
    y2Estimadoc3 = se3.tensaoEstimadac3
    
    x_pos = np.arange(len(barrax))
    
    #==============================================================================
    
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
    
    #==============================================================================
    
    y3Erroc1 = se1.erroEstimacaoTensaoc1
    y3Erroc2 = se2.erroEstimacaoTensaoc2
    y3Erroc3 = se3.erroEstimacaoTensaoc3
    
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

    #================================================
    
    mediaErroc1 = sum(se1.erroEstimacaoTensaoc1)/len(se1.erroEstimacaoTensaoc1)
    index_erroEstimacaoTensaoc1 = list(se1.erroEstimacaoTensaoc1).index(max(se1.erroEstimacaoTensaoc1))
    print("Cenário 1 - Erros SCADA", '\n')
    print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc1, 3))
    print("O maior erro percentual de tensão é:", '\n', round(se1.max_erroEstimacaoTensaoc1, 3))
    print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimacaoTensaoc1, '\n')

    mediaErroc2 = sum(se2.erroEstimacaoTensaoc2)/len(se2.erroEstimacaoTensaoc2)
    index_erroEstimacaoTensaoc2 = list(se2.erroEstimacaoTensaoc2).index(max(se2.erroEstimacaoTensaoc2))
    print("Cenário 2 - Erros SCADA sem redundância", '\n')
    print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc2, 3))
    print("O maior erro percentual de tensão é:", '\n', round(se2.max_erroEstimacaoTensaoc2, 3))
    print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimacaoTensaoc2, '\n')

    mediaErroc3 = sum(se3.erroEstimacaoTensaoc3)/len(se3.erroEstimacaoTensaoc3)
    index_erroEstimacaoTensaoc3 = list(se3.erroEstimacaoTensaoc3).index(max(se3.erroEstimacaoTensaoc3))
    print("Cenário 3 - Erros SCADA com redundância", '\n')
    print("A média dos erros percentuais de tensão é:", '\n', round(mediaErroc3, 3))
    print("O maior erro percentual de tensão é:", '\n', round(se3.max_erroEstimacaoTensaoc3, 3))
    print("O maior erro percentual de tensão é na barra:", '\n', index_erroEstimacaoTensaoc3, '\n')

else:
    #Histogramas =======================================================
    
    plt.hist(se1.listaErros1, bins=25, density=True, color='#ec622a')
    plt.xlabel('Erro (%)')
    plt.ylabel('Densidade de Frequência')
    plt.savefig("hist.pdf")
    plt.show()
    
    print("Cenário 1 - Erros SCADA", '\n')
    print("O maior erro de estimação em", g.N, "execuções foi de:", '\n', max(se1.listaErros1))
    print("A média dos erros nas", g.N, "execuções foi de:", '\n', np.mean(se1.listaErros1), '\n')
    
    #---------
    
    plt.hist(se2.listaErros2, bins=25, density=True, color='#50b580')
    plt.xlabel('Erro (%)')
    plt.ylabel('Densidade de Frequência')
    plt.savefig("hist.pdf")
    plt.show()
    
    print("Cenário 2 - Erros SCADA sem redundância", '\n')
    print("O maior erro de estimação em", g.N, "execuções foi de:", '\n', max(se2.listaErros2))
    print("A média dos erros nas", g.N, "execuções foi de:", '\n', np.mean(se2.listaErros2), '\n')
    
    #---------
    
    plt.hist(se3.listaErros3, bins=25, density=True, color='#5b00c2')
    plt.xlabel('Erro (%)')
    plt.ylabel('Densidade de Frequência')
    plt.savefig("hist.pdf")
    plt.show()
    
    print("Cenário 3 - Erros SCADA com redundância", '\n')
    print("O maior erro de estimação em", g.N, "execuções foi de:", '\n', max(se3.listaErros3))
    print("A média dos erros nas", g.N, "execuções foi de:", '\n', np.mean(se3.listaErros3), '\n')

