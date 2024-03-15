function res = ss_etmodelt(x)
alpha_ = 0.493; beta_ = 0.97; gamma_ = 0.41; delta_ = 0.1; eta_ = 0.667; omega_ = 0.349; Xi_ = -0.3828; stigma_ = 0.9979; phi_ = 5; rho_ = 0.9;
a = 1; b = 1; p = 1; Ga = 1; v = 1;
c = x(1); y = x(2); e = x(3); k = x(4); ke = x(5); L = x(6); i = x(7); w = x(8); r = x(9); co2 = x(10); g = x(11); d2 = x(12); f = x(13); q = x(14); xc = x(15);

res(1) = c + i - w*L - r*k;   % Eq.1
res(2) = k - (i + (1-delta_)*k);   % Eq.2
res(3) = w*(1-L) - eta_*c;   % Eq.3
res(4) = c - c*beta_*(1+r-delta_);   % Eq.4
res(5) = e - b*ke^gamma_;   % Eq.5
res(6) = r - gamma_*p*(e/ke);   % Eq.6
res(7) = r - alpha_*(y/k);   % Eq. 7    
res(8) = w - omega_*(y/L);   % Eq.8
res(9) = y - a*k^(alpha_)*L^(omega_)*e^(1-alpha_-omega_);   % Eq. 9
res(10) = g - Ga*co2;   % Eq.10
res(11) = d2*Ga*f - (1-alpha_-omega_)*(y/e);   % Eq.11
res(12) = co2 - d2*f*e;   % Eq.12
res(13) = f - Ga^Xi_;   % Eq.13
res(14) = q - rho_*q + co2 - phi_*v*g;   % Eq.14
res(15) = xc - stigma_*xc - co2;   % Eq.15
end