import createNetc1 as cnc1
import createNetc2 as cnc2
import createNetc3 as cnc3

N = 1

#%% Fluxo de Potência

tensaoRealc1 = cnc1.netc1.res_bus.vm_pu
anguloRealc1 = cnc1.netc1.res_bus.va_degree

tensaoRealc2 = cnc2.netc2.res_bus.vm_pu
anguloRealc2 = cnc2.netc2.res_bus.va_degree

tensaoRealc3 = cnc3.netc3.res_bus.vm_pu
anguloRealc3 = cnc3.netc3.res_bus.va_degree
