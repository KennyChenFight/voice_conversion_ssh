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
    server_source_wav_dir_path = '/home/voicetraining/merlin/egs/voice_conversion/s1/experiments/SF12TM1/test_synthesis/SF1'
    server_target_wav_dir_path = '/home/voicetraining/merlin/egs/voice_conversion/s1/experiments/SF12TM1/test_synthesis/TM1'
    convert_wav_command = 'cd merlin/egs/voice_conversion/s1/; bash /home/voicetraining/merlin/egs/voice_conversion/s1/run_final.sh SF1 TM1'

    @classmethod
    def upload_wav_to_server(cls):
        try:
            cls.sftp_upload_file()
            message = '上傳成功'
        except Exception:
            traceback.print_exc()
            message = '上傳失敗，請檢查連線'
        return message

    @classmethod
    def convert_wav(cls):
        try:
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

    @classmethod
    def download_wav_from_server(cls):
        try:
            cls.sftp_download_file()
            message = '下載成功'
        except:
            traceback.print_exc()
            message = '下載失敗，請檢查連線'
        return message

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

    @classmethod
    def remove_server_files_from_dir(cls, sftp):
        server_files = sftp.listdir(cls.server_source_wav_dir_path)
        for f in server_files:
            file_path = posixpath.join(cls.server_source_wav_dir_path, f)
            print(file_path)
            sftp.remove(file_path)
        server_files = sftp.listdir(cls.server_target_wav_dir_path)
        for f in server_files:
            file_path = posixpath.join(cls.server_target_wav_dir_path, f)
            print(file_path)
            sftp.remove(file_path)



