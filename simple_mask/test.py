

# clear all;
# close all;


fn_dir='/home/8ididata/2021-3/toney202110/cluster_results/';
fn = 'E005_D100_Lq1_025C_att03_001_0001-1000.hdf';

x_guess = 780.6;
y_guess = 259.4;

# % x_guess = 255;
# % y_guess = 507.3

full_hdf_filename = fullfile(fn_dir,fn);

a = loadhdf5result(full_hdf_filename);


X_E = double(h5read(full_hdf_filename,'/measurement/instrument/source_begin/energy'));

Det_Dist = double(h5read(full_hdf_filename,'/measurement/instrument/detector/distance'))/1000;
pix_size = double(h5read(full_hdf_filename,'/measurement/instrument/detector/x_pixel_size'))*1e-3;

lam = 12.398/X_E;
k0 = 2*pi/lam;

pix2q = (pix_size/Det_Dist)*k0;
 

img_2D = a.aIt{1};

figure;
imagesc(log(img_2D));
axis image;
axis xy;
colorbar

pix_pos_x = meshgrid(1:size(img_2D,2),1:size(img_2D,1));
pix_pos_y = meshgrid(1:size(img_2D,1),1:size(img_2D,2));



dim_x = 81;
dim_y = 91;
step_size = 0.1;

ROI_Dev=zeros(dim_x,dim_y);
x0=zeros(dim_x,1);
y0=zeros(dim_y,1);

for ii = 1:dim_x
    for jj = 1:dim_y
    
        x0(ii) = x_guess + (ii-floor(dim_x/2))*step_size;
        y0(jj) = y_guess + (jj-floor(dim_y/2))*step_size;
        Q_map = sqrt((pix_pos_x-x0(ii)).^2 + (pix_pos_y-y0(jj)).^2)*pix2q;

        Int_ROI = img_2D(Q_map>0.0065 & Q_map<0.0075);
        ROI_Dev(ii,jj) = var(Int_ROI)/mean(Int_ROI)/mean(Int_ROI);
        
    end
end

%%
figure;imagesc(x0,y0,ROI_Dev');axis image;axis xy;title('ROI Int. Var.');
colorbar;
% caxis([6e-2 6.2e-2]);



% figure;imagesc(pix_pos_x);axis image;axis xy;title('x');
% figure;imagesc(pix_pos_y);axis image;axis xy;title('y');

% figure;imagesc(Q_map);axis image;axis xy;title('Q');
% 
% check_ROI = zeros(size(img_2D,1),size(img_2D,2));
% check_ROI(Q_map>0.006 & Q_map<0.0062) = 10000;
% figure;imagesc(check_ROI);axis image;axis xy;title('Check ROI');


