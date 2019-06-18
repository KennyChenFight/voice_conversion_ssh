import posixpath
import paramiko
import traceback
import os


class SSH:
    host = '202.55.224.249'
    port = 22
    user = 'voicetraining'
    password = 'voice123!'
    local_source_wav_dir_path = 'source_wav/'
    local_target_wav_dir_path = 'target_wav/'
    model_name = ''
    server_source_wav_dir_path = '/home/voicetraining/merlin/egs/voice_conversion/s1/experiments/source2target/test_synthesis/source'
    server_target_wav_dir_path = '/home/voicetraining/merlin/egs/voice_conversion/s1/experiments/source2target/test_synthesis/target'
    convert_wav_command = 'cd merlin/egs/voice_conversion/s1/; bash /home/voicetraining/merlin/egs/voice_conversion/s1/run_final.sh source target'
    show_model_list_command = '/home/voicetraining/merlin/egs/voice_conversion/s1/'
    rename_model_to_experiments_command = 'cd merlin/egs/voice_conversion/s1/' + '; mv model experiments'
    rename_experiments_to_model_command = 'cd merlin/egs/voice_conversion/s1/' + '; mv experiments model'

    # 根據選擇的model動態變換路徑
    @classmethod
    def init_path(cls, model_name):
        cls.model_name = model_name
        old_experiments_name = cls.server_source_wav_dir_path.split('/')[-4]
        cls.server_source_wav_dir_path = cls.server_source_wav_dir_path.replace(old_experiments_name, model_name)
        cls.server_target_wav_dir_path = cls.server_target_wav_dir_path.replace(old_experiments_name, model_name)
        old_model_name = cls.rename_model_to_experiments_command.split(' ')[-2]
        cls.rename_model_to_experiments_command = cls.rename_model_to_experiments_command.replace(old_model_name, model_name)

    # 上傳wav到server
    @classmethod
    def upload_wav_to_server(cls):
        try:
            cls.sftp_upload_file()
            message = '上傳成功'
        except Exception:
            traceback.print_exc()
            message = '上傳失敗，請檢查連線'
        return message

    # 秀出model列表
    @classmethod
    def show_model_list(cls):
        try:
            t = paramiko.Transport((cls.host, cls.port))
            t.connect(username=cls.user, password=cls.password)
            sftp = paramiko.SFTPClient.from_transport(t)
            message = '連接成功'
            return message, sorted([name for name in sftp.listdir(cls.show_model_list_command) if name.startswith('model')], key=lambda x: int(x.replace('model_', '')))
        except:
            traceback.print_exc()
            message = '連接失敗'
            return message, []

    @classmethod
    def convert_wav(cls):
        try:
            cls.rename_model_name()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=cls.host, port=cls.port, username=cls.user, password=cls.password)
            stdin, stdout, stderr = ssh.exec_command(cls.convert_wav_command)
            print(stdout.read().decode('utf-8'))
            ssh.close()
            message = '轉換成功'
        except:
            message = '轉換失敗，請檢查連線'
            traceback.print_exc()
        return message

    # 將server的model資料夾改為experiments名稱
    @classmethod
    def rename_model_name(cls):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=cls.host, port=cls.port, username=cls.user, password=cls.password)
        stdin, stdout, stderr = ssh.exec_command(cls.rename_model_to_experiments_command)
        ssh.close()
        if (stderr.read().decode('utf-8') != ''):
            raise Exception

    # 將server的experiments資料夾改為原來model_name
    @classmethod
    def rename_experiments_name(cls):
        old_model_name = cls.rename_experiments_to_model_command.split(' ')[-1]
        cls.rename_experiments_to_model_command = cls.rename_experiments_to_model_command.replace(old_model_name, cls.model_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=cls.host, port=cls.port, username=cls.user, password=cls.password)
        stdin, stdout, stderr = ssh.exec_command(cls.rename_experiments_to_model_command)
        ssh.close()
        if (stderr.read().decode('utf-8') != ''):
            raise Exception

    # 從server上下載wav檔
    @classmethod
    def download_wav_from_server(cls):
        try:
            cls.rename_experiments_name()
            cls.sftp_download_file()
            message = '下載成功'
        except:
            traceback.print_exc()
            message = '下載失敗，請檢查連線'
        return message

    # local上傳檔案至server
    @classmethod
    def sftp_upload_file(cls):
        t = paramiko.Transport((cls.host, cls.port))
        t.connect(username=cls.user, password=cls.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        cls.remove_server_files_from_dir(sftp)
        local_wav_files = os.listdir(cls.local_source_wav_dir_path)
        for wav in local_wav_files:
             sftp.put(cls.local_source_wav_dir_path + '/' + wav, cls.server_source_wav_dir_path + '/' + wav)
        t.close()

    # server下載檔案至local
    @classmethod
    def sftp_download_file(cls):
        t = paramiko.Transport((cls.host, cls.port))
        t.connect(username=cls.user, password=cls.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        server_files = sftp.listdir(cls.server_target_wav_dir_path)
        for f in server_files:
            file_path = posixpath.join(cls.server_target_wav_dir_path, f)
            sftp.get(file_path, cls.local_target_wav_dir_path + f)
        t.close()

    # 在上傳音檔前，先將server上的所有舊的音檔先刪除
    @classmethod
    def remove_server_files_from_dir(cls, sftp):
        server_files = sftp.listdir(cls.server_source_wav_dir_path)
        for f in server_files:
            file_path = posixpath.join(cls.server_source_wav_dir_path, f)
            sftp.remove(file_path)
        server_files = sftp.listdir(cls.server_target_wav_dir_path)
        for f in server_files:
            file_path = posixpath.join(cls.server_target_wav_dir_path, f)
            sftp.remove(file_path)




