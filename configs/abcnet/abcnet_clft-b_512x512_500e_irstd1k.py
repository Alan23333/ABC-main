_base_ = [
    'abcnet_clft-s_512x512_500e_irstd1k.py'
]

model = dict(
    decode_head=dict(
        dim=32
    )
)
data = dict(train_batch=16)