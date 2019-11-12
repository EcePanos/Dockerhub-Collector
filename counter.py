import json
import csv
from datetime import date
import matplotlib.pyplot as plt


def count(filename):
    with open(filename) as input:
        data = json.load(input)

    tag_count = 0
    image_count = 0
    latest_images = 0
    arm_images = 0
    arm64_images = 0
    ppc64le_images = 0
    x386_images = 0
    amd64_images = 0
    s390x_images = 0
    linux_images = 0
    windows_images = 0
    for entry in data:
        tag_count += len(data[entry]['results'])
        for result in data[entry]['results']:
            image_count += len(result['images'])
            if result['name'] == 'latest':
                latest_images += len(result['images'])
            for image in result['images']:
                if image['architecture'] == 'arm':
                    arm_images += 1
                elif image['architecture'] == 'arm64':
                    arm64_images += 1
                elif image['architecture'] == 'ppc64le':
                    ppc64le_images += 1
                elif image['architecture'] == '386':
                    x386_images += 1
                elif image['architecture'] == 'amd64':
                    amd64_images += 1
                elif image['architecture'] == 's390x':
                    s390x_images += 1
                if image['os'] == 'linux':
                    linux_images += 1
                elif image['os'] == 'windows':
                    windows_images += 1
                if image['os'] not in ['linux', 'windows', '', None]:
                    print(image['os'])
                if image['os_features'] not in ['', None]:
                    print(image['os_features'])

    with open('data/report-{}.txt'.format(str(date.today())), 'w') as f:
        f.write("########################################\n")
        f.write("General info\n")
        f.write("########################################\n")
        f.write("Number of repos: " + str(len(data)) + "\n")
        f.write("Number of tags: " + str(tag_count) + "\n")
        f.write("Number of images: " + str(image_count) + "\n")
        f.write("Images tagged 'latest': " + str(latest_images) + "\n")
        f.write("########################################" + "\n")
        f.write("Architectures" + "\n")
        f.write("########################################" + "\n")
        f.write("ARM images: " + str(arm_images) + " " + str(round(arm_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("ARM 64 images: " + str(arm64_images) + " " + str(round(arm64_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("PowerPC 64 LE images: " + str(ppc64le_images) + " " + str(round(ppc64le_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("x86 images: " + str(x386_images) + " " + str(round(x386_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("x86-64 images: " + str(amd64_images) + " " + str(round(amd64_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("s390x images: " + str(s390x_images) + " " + str(round(s390x_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("########################################" + "\n")
        f.write("Operating systems" + "\n")
        f.write("########################################" + "\n")
        f.write("Linux images: " + str(linux_images) + " " + str(round(linux_images/image_count*100, 2)) + "% of total" + "\n")
        f.write("Windows images: " + str(windows_images) + " " + str(round(windows_images/image_count*100, 2)) + "% of total" + "\n")


    with open('data/output-{}.json'.format(str(date.today())), 'w') as output:
        json.dump(data, output, indent=4)

    labels = 'ARM', 'ARM64', 'PPC64LE', 'x86', 'AMD64', 'IBM Z'
    sizes = [arm_images, arm64_images, ppc64le_images, x386_images, amd64_images, s390x_images]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('data/architectures-{}.png'.format(str(date.today())))

    plt.clf()

    labels2 = 'Linux', 'Windows'
    sizes2 = [linux_images, windows_images]

    plt.pie(sizes2, labels=labels2, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('data/os-{}.png'.format(str(date.today())))

    plt.clf()

    with open('data/control-' + str(date.today()) + '.csv', 'w') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([image_count])
