% Parameter
r1 = 0.1;   % Pertumbuhan populasi x
r2 = 0.3;  % Pertumbuhan populasi y
a1 = 0.05;  % Kompetisi populasi x
a2 = 0.01;  % Kompetisi populasi y
v1 = 0.01; % Interaksi antara x dan y
v2 = 0.03; % Interaksi antara y dan x

% Sistem persamaan diferensial
dxdt = @(t, X) [r1*X(1) - a1*X(1)^2 - v1*X(1)*X(2); 
                r2*X(2) - a2*X(2)^2 - v2*X(1)*X(2)];

% Kondisi awal
x0 = [10; 5]; % x(0) = [mangsa;predator]
tspan = [0 50]; % Rentang waktu

% Solusi numerik menggunakan ode45
[t, X] = ode45(dxdt, tspan, x0);

% Plot x(t) dan y(t) terhadap waktu
figure;
plot(t, X(:, 1), 'r-', 'LineWidth', 2); hold on;
plot(t, X(:, 2), 'g--', 'LineWidth', 2);
xlabel('Waktu (t)');
ylabel('Populasi');
legend('x(t) (Mangsa)', 'y(t) (Predator)');
title('Evolusi Populasi Predator-Prey');
grid on;

% Plot diagram fase (x vs y)
figure;
plot(X(:, 1), X(:, 2), 'b-', 'LineWidth', 2);
xlabel('Populasi Mangsa, x');
ylabel('Populasi Predator, y');
title('Diagram Fase Predator-Prey');
grid on;
