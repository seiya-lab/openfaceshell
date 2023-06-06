import tkinter as tk
from tkinter import filedialog

def select_path(is_folder=False):
    root = tk.Tk()
    root.withdraw()  # ���C���E�B���h�E���\���ɂ���

    try:
        if is_folder:
            path = filedialog.askdirectory()  # �t�H���_��I������_�C�A���O��\������
        else:
            path = filedialog.askopenfilename()  # �t�@�C����I������_�C�A���O��\������
        
        # �I�����L�����Z�����ꂽ�ꍇ�͋�̕������Ԃ�
        if not path:
            return ""
        
        # �I�����ꂽ�p�X��Ԃ�
        return path

    except Exception as e:
        # �G���[���b�Z�[�W��\�����Ă����O���ăX���[����
        error_message = f"Error: {e}"
        raise ValueError(error_message)