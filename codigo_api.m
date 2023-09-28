function out = fcn(Va,Vb,Vc,Ts,fg,percent)

persistent theta_e0 u_vco0 u0 theta_grid w_grid  u_vco u  Kp wg_min up ui ui0 u0psat upsat u0sat
persistent theta_e Vdf  Vqf theta_grid_estimado alfa w_max alfaf Kp_min  usat
 
if isempty(theta_e)
    theta_e0=0; u_vco0=0; u0=0;
    w_grid = 0;theta_grid = 0; w_grid = 0; u_vco = 0; u = 0;up = 0; ui = 0; u0psat = 0; upsat = 0; u0sat = 0;
    ui0 = 0;usat = 0;
    Vdf = 0; Vqf = 0;theta_grid_estimado = 0;alfa = 1;Kp = 0;
    theta_e = 0;w_max = 2*pi*60;alfaf = 1;wg_min = 0;Kp_min = 0;
end
Vab = Va - Vb;
Vbc = Vb - Vc;

Va = 2/3*Vab + 1/3*Vbc;
Vb = -1/3*Vab + 1/3*Vbc;
Vc = -1/3*Vab - 2/3*Vbc;
%Calcula Vd e Vq
Valfa = 2/3*Va -1/3*Vb - 1/3*Vc;
Vbeta = (1/sqrt(3))*Vb -(1/sqrt(3))*Vc;

vd = Valfa*cos(theta_grid-pi/2) + Vbeta*sin(theta_grid-pi/2);
vq = -Valfa*sin(theta_grid-pi/2) + Vbeta*cos(theta_grid-pi/2);

wc = w_grid;
tau = abs(2/(wc+0.1));
a = Ts/(tau);

Vdf = (1-a)*Vdf + a*vd;
Vqf = (1-a)*Vqf+ a*vq;


%Calcula theta_e = atan2(Vq/Vd)
theta_e = atan2(Vqf,Vdf);
%Estima frequencia com estrutua de controle PI*/
wg_min = w_grid*0.2;
% if w_grid <= 0.2*100*2*pi
%     Kp_min = 60;
% % elseif w_grid >= 0.8*100*2*pi
% %     Kp_min = 112;
% else
% Kp_min = (w_grid - wg_min)/pi;
% end
Kp_min = (w_grid - wg_min)/pi

if Kp_min>= 30
  Kp_min = 30;
end

Kp = 80;
up = Kp*theta_e;
ui = ui0 + 20*Kp_min*Ts*theta_e;
%u = u0 + Kp*(theta_e-theta_e0) + 10*Kp_min*Ts*theta_e;
u = up + ui;
w_grid = u;
u_vco = u_vco0 + Ts*w_grid;
theta_grid = u_vco;
theta_grid_estimado = theta_grid + theta_e;
u_vco0 = u_vco;
theta_e0 = theta_e;
u0 = u;
ui0 = ui;
out = [theta_grid_estimado;theta_e;w_grid;vd;vq;Kp_min];