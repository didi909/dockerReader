import json
import os
import sys

def readInspect(container_name):
    base_shell='docker inspect'
    total_shell=base_shell+' '+container_name
    result=os.popen(total_shell).read()

    status=os.wait()[1]
    if status == 0:
        #判断执行结果
        result_dict = json.loads(result)[0]

        #镜像
        c_image=result_dict['Config']['Image']
        #print(c_image)

        #容器名称，单一
        c_name=result_dict['Name'][1:]
        #print(c_name)

        #绑定信息，多条
        c_bind=''
        if result_dict['HostConfig']['Binds'] != None:
            for bind in result_dict['HostConfig']['Binds']:
                c_bind=c_bind+' -v '+bind
        #print(c_bind)

        #网络信息
        c_network=result_dict['HostConfig']['NetworkMode']
        #print(c_network)

        #Cmd
        c_cmd=''
        if result_dict['Config']['Cmd'] != None:
            for cmd in result_dict['Config']['Cmd']:
                c_cmd=c_cmd+' '+cmd
        #print(c_cmd)

        #docker command
        print('docker run -d --name=%s --network==%s %s %s %s' % (c_name,c_network,c_bind,c_image,c_cmd))
    else:
        print('脚本执行异常')

def usage(filename):
    print('用法：')
    print('    python %s container_name' % filename)

if __name__ == '__main__':
    py_name=os.path.basename(sys.argv[0])
    if len(sys.argv) != 2:
        usage(py_name)
    else:
        readInspect(sys.argv[1])