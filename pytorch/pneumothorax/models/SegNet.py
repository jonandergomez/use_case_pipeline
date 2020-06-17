import torch.nn as nn


class SegNet(nn.Module):
    def __init__(self):
        super(SegNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(64, momentum=0.1)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64, momentum=0.1)
        self.maxpool1 = nn.MaxPool2d(2, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128, momentum=0.1)
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1)
        self.bn4 = nn.BatchNorm2d(128, momentum=0.1)
        self.maxpool2 = nn.MaxPool2d(2, stride=2)
        self.conv5 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1)
        self.bn5 = nn.BatchNorm2d(256, momentum=0.1)
        self.conv6 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
        self.bn6 = nn.BatchNorm2d(256, momentum=0.1)
        self.conv7 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
        self.bn7 = nn.BatchNorm2d(256, momentum=0.1)

        self.maxpool3 = nn.MaxPool2d(2, stride=2)
        self.conv8 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1)
        self.bn8 = nn.BatchNorm2d(512, momentum=0.1)

        self.conv9 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn9 = nn.BatchNorm2d(512, momentum=0.1)

        self.conv10 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn10 = nn.BatchNorm2d(512, momentum=0.1)
        self.maxpool4 = nn.MaxPool2d(2, stride=2)
        self.conv11 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn11 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv12 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn12 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv13 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn13 = nn.BatchNorm2d(512, momentum=0.1)
        self.maxpool5 = nn.MaxPool2d(2, stride=2)
        self.upsampling1 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv14 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn14 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv15 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn15 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv16 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn16 = nn.BatchNorm2d(512, momentum=0.1)
        self.upsampling2 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv17 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn17 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv18 = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=3, padding=1)
        self.bn18 = nn.BatchNorm2d(512, momentum=0.1)
        self.conv19 = nn.Conv2d(in_channels=512, out_channels=256, kernel_size=3, padding=1)
        self.bn19 = nn.BatchNorm2d(256, momentum=0.1)
        self.upsampling3 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv20 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
        self.bn20 = nn.BatchNorm2d(256, momentum=0.1)
        self.conv21 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)
        self.bn21 = nn.BatchNorm2d(256, momentum=0.1)
        self.conv22 = nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, padding=1)
        self.bn22 = nn.BatchNorm2d(128, momentum=0.1)
        self.upsampling4 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv23 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1)
        self.bn23 = nn.BatchNorm2d(128, momentum=0.1)
        self.conv24 = nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, padding=1)
        self.bn24 = nn.BatchNorm2d(64, momentum=0.1)
        self.upsampling5 = nn.Upsample(scale_factor=2, mode='nearest')
        self.conv25 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1)
        self.bn25 = nn.BatchNorm2d(64, momentum=0.1)
        self.conv_final = nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, padding=1)

        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.maxpool1(x)

        x = self.relu(self.bn3(self.conv3(x)))
        x = self.relu(self.bn4(self.conv4(x)))
        x = self.maxpool2(x)

        x = self.relu(self.bn5(self.conv5(x)))
        x = self.relu(self.bn6(self.conv6(x)))
        x = self.relu(self.bn7(self.conv7(x)))
        x = self.maxpool3(x)

        x = self.relu(self.bn8(self.conv8(x)))
        x = self.relu(self.bn9(self.conv9(x)))
        x = self.relu(self.bn10(self.conv10(x)))
        x = self.maxpool4(x)

        x = self.relu(self.bn11(self.conv11(x)))
        x = self.relu(self.bn12(self.conv12(x)))
        x = self.relu(self.bn13(self.conv13(x)))
        x = self.maxpool5(x)

        x = self.upsampling1(x)

        x = self.relu(self.bn14(self.conv14(x)))
        x = self.relu(self.bn15(self.conv15(x)))
        x = self.relu(self.bn16(self.conv16(x)))
        x = self.upsampling2(x)

        x = self.relu(self.bn17(self.conv17(x)))
        x = self.relu(self.bn18(self.conv18(x)))
        x = self.relu(self.bn19(self.conv19(x)))
        x = self.upsampling3(x)

        x = self.relu(self.bn20(self.conv20(x)))
        x = self.relu(self.bn21(self.conv21(x)))
        x = self.relu(self.bn22(self.conv22(x)))
        x = self.upsampling4(x)

        x = self.relu(self.bn23(self.conv23(x)))
        x = self.relu(self.bn24(self.conv24(x)))
        x = self.upsampling5(x)

        x = self.relu(self.bn25(self.conv25(x)))
        x = self.conv_final(x)

        return self.sigmoid(x)