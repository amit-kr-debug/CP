# Avalanche effect
proc_seq = ""
all = [
    'new','block_size','key_size',
    'MODE_ECB','MODE_CBC','MODE_CFB','MODE_OFB','MODE_CTR'
]

SBOX = (
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,
    0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,
    0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,
    0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,
    0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,
    0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,
    0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,
    0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,
    0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,
    0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,
    0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,
    0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,
    0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,
    0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,
    0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,
    0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,
    0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16,
)
INV_SBOX = (
    0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,
    0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb,
    0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,
    0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb,
    0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,
    0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e,
    0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,
    0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25,
    0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,
    0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92,
    0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,
    0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84,
    0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,
    0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06,
    0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,
    0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b,
    0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,
    0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73,
    0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,
    0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e,
    0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,
    0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b,
    0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,
    0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4,
    0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,
    0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f,
    0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,
    0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef,
    0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,
    0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61,
    0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,
    0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d,
)

round_constants = (0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36)

MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_PGP = 4  # optional
MODE_OFB = 5
MODE_CTR = 6


class BlockCipher:

    def encrypt_block(self,block):
        raise NotImplementedError

    def decrypt_block(self,block):
        raise NotImplementedError


# <removed lines of code>


class Counter:

    def init(self,nonce,block_size,byte_order='big'):
        self.nonce = nonce
        self.counter_size = block_size - len(nonce)
        self.byte_order = byte_order
        self.counter = 0

    def call(self):
        out = self.nonce + self.counter.to_bytes(
            self.counter_size,self.byte_order
        )
        self.counter += 1
        return out


class BlockCipherWrapper:

    def init(self):
        """initiate instance attributes."""
        # PEP 272 required attributes
        self.block_size: int = NotImplemented  # measured in bytes
        self.IV: bytes = NotImplemented  # initialization vector
        # other attributes
        self.mode: int = NotImplemented
        self.cipher: BlockCipher = NotImplemented
        self.counter: Counter = NotImplemented
        self.segment_size: int = NotImplemented

    def encrypt(self,byte_string):

        if self.mode == MODE_CFB and len(byte_string) * 8 % self.segment_size:
            raise ValueError("message length doesn't match segment size")
        if self.mode == MODE_CFB and self.segment_size & 7:
            raise NotImplementedError
        if self.mode != MODE_CFB and len(byte_string) % self.block_size:
            raise ValueError("message length doesn't match block size")

        blocks = [
            byte_string[i:i + self.block_size]
            for i in range(0,len(byte_string),self.block_size)
        ]

        if self.mode == MODE_ECB:
            return b''.join([
                self.cipher.encrypt_block(block) for block in blocks
            ])
        elif self.mode == MODE_CBC:
            cipher_blocks = [self.IV]
            for block in blocks:
                cipher_blocks.append(
                    self.cipher.encrypt_block(
                        self.xor(block,cipher_blocks[-1])
                    )
                )
            return b''.join(cipher_blocks[1:])
        elif self.mode == MODE_CFB:
            s = self.segment_size >> 3
            cipher = b''
            current_input = self.IV
            while byte_string:
                cipher += self.xor(
                    byte_string[:s],
                    self.cipher.encrypt_block(current_input)[:s]
                )
                byte_string = byte_string[s:]
                current_input = current_input[s:] + cipher[-s:]
            return cipher
        elif self.mode == MODE_PGP:
            raise NotImplementedError
        elif self.mode == MODE_OFB:
            last_output = self.IV
            cipher_blocks = [self.IV]
            for block in blocks:
                last_output = self.cipher.encrypt_block(last_output)
                cipher_blocks.append(self.xor(block,last_output))
            return b''.join(cipher_blocks[1:])
        elif self.mode == MODE_CTR:
            cipher_blocks = []
            for block in blocks:
                ctr = self.counter()
                if len(ctr) != self.block_size:
                    raise ValueError("counter has the wrong size")
                cipher_blocks.append(
                    self.xor(self.cipher.encrypt_block(ctr),block)
                )
            return b''.join(cipher_blocks)
        else:
            raise NotImplementedError("This mode is not supported")

    def xor(self,block1,block2):

        size = (
            self.segment_size >> 3
            if self.mode == MODE_CFB
            else self.block_size
        )
        if not (len(block1) == len(block2) == size):
            raise ValueError(str(size))
        return bytes([block1[i] ^ block2[i] for i in range(size)])


block_size = 16
key_size = None


def new(key,mode,IV=None,**kwargs) -> BlockCipherWrapper:
    if mode in (MODE_CBC,MODE_CFB,MODE_OFB) and IV is None:
        raise ValueError("This mode requires an IV")

    cipher = BlockCipherWrapper()
    cipher.block_size = block_size
    cipher.IV = IV
    cipher.mode = mode
    cipher.cipher = AES(key)

    if mode == MODE_CFB:
        cipher.segment_size = kwargs.get('segment_size',block_size * 8)
    elif mode == MODE_CTR:
        counter = kwargs.get('counter')
        if counter is None:
            raise ValueError("CTR mode requires a callable counter object")
        cipher.counter = counter

    return cipher


class AES(BlockCipher):

    def __init__(self,key):

        self.key = key
        self.Nk = len(self.key) // 4  # words per key
        if self.Nk not in (4,6,8):
            raise ValueError("invalid key size")
        self.Nr = self.Nk + 6
        self.Nb = 4  # words per block
        self.state: list[list[int]] = []
        # raise NotImplementedError
        # key schedule
        self.w: list[list[int]] = []
        for i in range(self.Nk):
            self.w.append(list(key[4 * i:4 * i + 4]))
        for i in range(self.Nk,self.Nb * (self.Nr + 1)):
            tmp: list[int] = self.w[i - 1]
            q,r = divmod(i,self.Nk)
            if not r:
                tmp = self.sub_word(self.rot_word(tmp))
                tmp[0] ^= round_constants[q - 1]
            elif self.Nk > 6 and r == 4:
                tmp = self.sub_word(tmp)
            self.w.append(
                [a ^ b for a,b in zip(self.w[i - self.Nk],tmp)]
            )

    def print_data(self,round,str1,str2,str3):

        encry_process = ""
        encry_process += "\n"
        temp_space = "         "
        if round == 10:
            temp_space = "        "
        if round == 0:
            round = "Pre-round"
            encry_process += str(round) + "   "
        else:
            encry_process += "  " + str(round) + temp_space
        st_space = "            "

        tab = " "
        line1 = str1[:2] + tab + str1[8:10] + tab + str1[16:18] + tab + str1[24:26] + "       " + str2[:2] + tab + str2[
                                                                                                                   8:10] + tab + str2[
                                                                                                                                 16:18] + tab + str2[
                                                                                                                                                24:26] + "       " + str3[
                                                                                                                                                                     :2] + tab + str3[
                                                                                                                                                                                 8:10] + tab + str3[
                                                                                                                                                                                               16:18] + tab + str3[
                                                                                                                                                                                                              24:26]
        line2 = str1[2:4] + tab + str1[10:12] + tab + str1[18:20] + tab + str1[26:28] + "       " + str2[
                                                                                                    2:4] + tab + str2[
                                                                                                                 10:12] + tab + str2[
                                                                                                                                18:20] + tab + str2[
                                                                                                                                               26:28] + "       " + str3[
                                                                                                                                                                    2:4] + tab + str3[
                                                                                                                                                                                 10:12] + tab + str3[
                                                                                                                                                                                                18:20] + tab + str3[
                                                                                                                                                                                                               26:28]
        line3 = str1[4:6] + tab + str1[12:14] + tab + str1[20:22] + tab + str1[28:30] + "       " + str2[
                                                                                                    4:6] + tab + str2[
                                                                                                                 12:14] + tab + str2[
                                                                                                                                20:22] + tab + str2[
                                                                                                                                               28:30] + "       " + str3[
                                                                                                                                                                    4:6] + tab + str3[
                                                                                                                                                                                 12:14] + tab + str3[
                                                                                                                                                                                                20:22] + tab + str3[
                                                                                                                                                                                                               28:30]
        line4 = str1[6:8] + tab + str1[14:16] + tab + str1[22:24] + tab + str1[30:32] + "       " + str2[
                                                                                                    6:8] + tab + str2[
                                                                                                                 14:16] + tab + str2[
                                                                                                                                22:24] + tab + str2[
                                                                                                                                               30:32] + "       " + str3[
                                                                                                                                                                    6:8] + tab + str3[
                                                                                                                                                                                 14:16] + tab + str3[
                                                                                                                                                                                                22:24] + tab + str3[
                                                                                                                                                                                                               30:32]
        encry_process += line1.upper() + "\n"

        encry_process += st_space

        encry_process += line2.upper() + "\n"

        encry_process += st_space

        encry_process += line3.upper() + "\n"

        encry_process += st_space

        encry_process += line4.upper() + "\n"

        encry_process += "\n"

        return encry_process

    def encrypt_block(self,block):

        encr_process = "\n"
        encr_process += "Round       Input State       Output state       Round key\n"

        self.set_state(block)
        round_key_vals = self.add_round_key(0)
        output_state = self.get_state().hex()
        encr_process += self.print_data(0,str(block.hex()),str(output_state),round_key_vals)

        block = output_state
        for r in range(1,self.Nr):
            self.sub_bytes()
            self.shift_rows()
            self.mix_columns()
            round_key_vals = self.add_round_key(r)

            output_state = self.get_state().hex()
            encr_process += self.print_data(r,block,str(output_state),round_key_vals)

            block = output_state
        self.sub_bytes()
        self.shift_rows()
        round_key_vals = self.add_round_key(self.Nr)

        output_state = self.get_state().hex()
        encr_process += self.print_data(10,block,str(output_state),round_key_vals)

        global proc_seq
        proc_seq = encr_process
        return self.get_state()

    def decrypt_block(self,block):

        self.set_state(block)
        self.add_round_key(self.Nr)
        for r in range(self.Nr - 1,0,-1):
            self.inv_shift_rows()
            self.inv_sub_bytes()
            self.add_round_key(r)
            self.inv_mix_columns()
        self.inv_shift_rows()
        self.inv_sub_bytes()
        self.add_round_key(0)
        return self.get_state()

    @staticmethod
    def rot_word(word):
        # for key schedule
        return word[1:] + word[:1]

    @staticmethod
    def sub_word(word):
        # for key schedule
        return [SBOX[b] for b in word]

    def set_state(self,block: bytes):

        self.state = [
            list(block[i:i + 4])
            for i in range(0,16,4)
        ]

    def get_state(self):

        return b''.join(
            bytes(col)
            for col in self.state
        )

    def add_round_key(self,r):

        round_key = self.w[r * self.Nb:(r + 1) * self.Nb]

        for col,word in zip(self.state,round_key):
            for row_index in range(4):
                col[row_index] ^= word[row_index]
        round_key_vals = [[str(hex(x))[2:] for x in y] for y in round_key]
        for i in range(4):
            for j in range(4):
                if len(round_key_vals[i][j]) == 1:
                    round_key_vals[i][j] = "0" + round_key_vals[i][j]

        round_key_vals_to_Str = ""
        for arr in round_key_vals:
            round_key_vals_to_Str += "".join(arr)
        return round_key_vals_to_Str

    def mix_columns(self):

        for i,word in enumerate(self.state):
            new_word = []
            for j in range(4):
                # element wise cl mul with constants 2, 3, 1, 1
                value = (word[0] << 1)
                value ^= (word[1] << 1) ^ word[1]
                value ^= word[2] ^ word[3]
                # polynomial reduction in constant time
                value ^= 0x11b & -(value >> 8)
                new_word.append(value)
                # rotate word in order to match the matrix multiplication
                word = self.rot_word(word)
            self.state[i] = new_word

    def shift_rows(self):

        for row_index in range(4):
            row = [
                col[row_index] for col in self.state
            ]
            row = row[row_index:] + row[:row_index]
            for col_index in range(4):
                self.state[col_index][row_index] = row[col_index]

    def sub_bytes(self):

        for col in self.state:
            for row_index in range(4):
                col[row_index] = SBOX[col[row_index]]


# Avalanche Effect
plain_text1 = input("Plain Text 1  :   ")  # 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
plain_text2 = input("Plain Text 2  :   ")  # 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01
print()
# print("Plain Text 1  :   ", plain_text1)
# print("Plain Text 2  :   ", plain_text2)
plain_text1 = bytes.fromhex(plain_text1)  # 32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34
plain_text2 = bytes.fromhex(plain_text2)
key = '24 75 A2 B3 34 75 56 88 31 E2 12 00 13 AA 54 87'
# print("Cipher key   :   ", key)
key = bytes.fromhex(key)  # 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c
cipher = new(key,MODE_ECB)
cipher_text1 = cipher.encrypt(plain_text1)
cipher_text2 = cipher.encrypt(plain_text2)
cipher_text_hex1 = cipher_text1.hex()
cipher_text_hex2 = cipher_text2.hex()
temp1 = str(cipher_text_hex1).upper()
temp2 = str(cipher_text_hex2).upper()
cipher_text_hex1 = ""
cipher_text_hex2 = ""
for i in range(0,len(temp1),2):
    cipher_text_hex1 += temp1[i:i + 2] + " "
print("Cipher Text 1  :   ",cipher_text_hex1)
for i in range(0,len(temp2),2):
    cipher_text_hex2 += temp2[i:i + 2] + " "
print("Cipher Text 2  :   ",cipher_text_hex2)