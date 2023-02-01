% matlab计算灰度共生矩阵

i = getFolders("../My_image/group_tape_stripping_numbers/");
GLCMFeatures_sum = [];
for j = 1:length(i)
    GLCMFeatures = showImage(i(j).name);
    GLCMFeatures_sum = [GLCMFeatures_sum; GLCMFeatures];
end
% 保存mat文件
save("../Result_Images/GLCM/GLCMFeatures_sum.mat", "GLCMFeatures_sum")
% 可视化
function [GLCMFeatures] = showImage(path)
    path1 = strcat("../My_image/group_tape_stripping_numbers/", path);
    files = getFiles(path1);

    GLCMFeatures = [];
    for i = 1:length(files)
        [contrast, correlation, energy, homogeneity] = getGLCMFeatures(strcat(path1,"/",files(i).name));
        % 切割字符串
        % str = files(i).name;
        % str = strsplit(str, '.');
        % str = str{1};
        % str = strsplit(str, '_');
        % image_num = strcat(str(1), str(2), str(3), str(4));
        % GLCMFeatures = [GLCMFeatures; image_num, contrast.Contrast, correlation.Correlation, energy.Energy, homogeneity.Homogeneity];
        GLCMFeatures = [GLCMFeatures; contrast.Contrast, correlation.Correlation, energy.Energy, homogeneity.Homogeneity];
    end
    disp(GLCMFeatures);

    


    % 每列归一化
    % GLCMFeatures = GLCMFeatures ./ max(GLCMFeatures, [], 1);
    % disp(GLCMFeatures);

    % 每行累加
    % GLCMFeatures_row = sum(GLCMFeatures, 2);
    % disp(GLCMFeatures_row);
    

    % 画四幅图
    x = 0:2:8;
    figure(1)
    title(path)
    subplot(2,2,1)
    plot(x, GLCMFeatures(:,1))
    title('contrast')
    subplot(2,2,2)
    plot(x, GLCMFeatures(:,2))
    title('correlation')
    subplot(2,2,3)
    plot(x, GLCMFeatures(:,3))
    title('energy')
    subplot(2,2,4)
    plot(x, GLCMFeatures(:,4))
    title('homogeneity')
    path1 = strsplit(path, '.');
    path1 = strsplit(path1{1}, '_');
    sgtitle(strcat(path1{1},path1{2},path1{3}));

    % 保存图片
    saveas(gcf, strcat("../Result_Images/GLCM/", path, ".png"))
end


% 抽象成函数
function [contrast, correlation, energy, homogeneity] = getGLCMFeatures(path)   
    
    I = imread(path);
    I = rgb2gray(I);
    image_size = size(I);
    % 提取图像核心区域
    I_resize = I(image_size(1)/4:image_size(1)*3/4, image_size(2)/4:image_size(2)*3/4); 

    % GLCM = graycomatrix(I_resize,'Offset',[0 1]);
    GLCM = graycomatrix(I_resize,'Offset',[0 1]);
    contrast = graycoprops(GLCM,'Contrast');
    correlation = graycoprops(GLCM,'Correlation');
    energy = graycoprops(GLCM,'Energy');
    homogeneity = graycoprops(GLCM,'Homogeneity');
end

% 获取文件夹下的文件
function [files] = getFiles(path)
    files = dir(path);
    files = files(3:end);
end

% 获取文件夹下的文件夹名字
function [folders] = getFolders(path)
    folders = dir(path);
    folders = folders(3:end);
end






