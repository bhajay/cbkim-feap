%% CB-KIM Basis Vector Determination
clc;clear all; close all;
% lattice parameters
I=2; 
J=2; 
K=2;

% number of atoms in a unit cell
n=2; 

% define material numbers
Si=14;

% define storage vector for all atom locations in basis
r_atoms_all = zeros(I*J*K*n,4);

%% Define Unit Cell Basis
% define the unit cell basis vectors (non-orthogonal basis)
a1 = [0.0000000000000000E+00; 0.2715474887350542E+01; 0.2715474887350542E+01;];
a2 = [0.2715474887350542E+01; 0.0000000000000000E+00; 0.2715474887350542E+01];
a3 = [.2715474887350542E+01; 0.2715474887350542E+01; 0.0000000000000000E+00];

% Cell plot arrays
X = [0, a1(1), a1(1)+a2(1), a2(1), 0, 0+a3(1), a1(1)+a3(1), a1(1)+a2(1)+a3(1), a2(1)+a3(1), 0+a3(1), a2(1)+a3(1), a2(1), a1(1)+a2(1), a1(1)+a2(1)+a3(1), a1(1)+a3(1), a1(1)];
Y = [0, a1(2), a1(2)+a2(2), a2(2), 0, 0+a3(2), a1(2)+a3(2), a1(2)+a2(2)+a3(2), a2(2)+a3(2), 0+a3(2), a2(2)+a3(2), a2(2), a1(2)+a2(2), a1(2)+a2(2)+a3(2), a1(2)+a3(2), a1(2)];
Z = [0, a1(3), a1(3)+a2(3), a2(3), 0, 0+a3(3), a1(3)+a3(3), a1(3)+a2(3)+a3(3), a2(3)+a3(3), 0+a3(3), a2(3)+a3(3), a2(3), a1(3)+a2(3), a1(3)+a2(3)+a3(3), a1(3)+a3(3), a1(3)];


%Scaled Basis for CBKIM input file
a_basis_scaled = [I*a1';J*a2';K*a3'];

%% Loop over IJK to construct lattice
% define atom locations in the unit cell
r1 = [0.0000000000000000E+00; 0.0000000000000000E+00; 0.0000000000000000E+00];
r2 = [0.1357737443675271E+01; 0.1357737443675271E+01; 0.1357737443675271E+01];
r_unit_atoms = [r1, r2];

m=1;
for i = 1:1:I
    for j = 1:1:J
        for k = 1:1:K
            Rc = (i-1)*a1 + (j-1)*a2 + (k-1)*a3;
            for p = 1:1:n
                R = Rc + r_unit_atoms(:,p);
                r_atoms_all(m,:)=[Si, R'];
                plot3(R(1),R(2),R(3),'bo','Markersize',15,'MarkerFaceColor',...
                    [1*p/n,0.2,0.2]); hold on; grid on; axis equal;  % mod color on the basis atoms
                m=m+1;
            end
            % Drawline connecting the TWO atoms in the basis
            plot3(r_atoms_all((m-2):(m-1),2),r_atoms_all((m-2):(m-1),3),r_atoms_all((m-2):(m-1),4),'-k');
            % Plot lattice cell
            plot3(X+Rc(1),Y+Rc(2),Z+Rc(3),'-b')
        end
    end
end
plot3(X,Y,Z,'-b')
%% Export Atom Locations to a Text file
format long
fileID1 = fopen('atoms.txt','w');
formatSpec = '%d %.8f %.8f %.8f\n';
[nrows,ncols] = size(r_atoms_all);
for row = 1:nrows
    fprintf(fileID1,formatSpec,r_atoms_all(row,:));
end
fclose(fileID1);

%% Export Scaled Basis to a Text file
format long
fileID2 = fopen('scaled_basis.txt','w');
formatSpec = '%.8f  %.8f %.8f\n';
[nrows,ncols] = size(a_basis_scaled);
for row = 1:nrows
    fprintf(fileID2,formatSpec,a_basis_scaled(row,:));
end
fclose(fileID2);
