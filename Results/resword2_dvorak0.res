�]q (]q]q(}q(X
   beams_sizeqKX
   sample_maxqKX   temperatureqG?�      X   flipqK X   start_from_bestqK X
   start_fromq	NX   configq
X*   config/sample2_tfidf_freq_tword20_a05.yamlqX	   modelnameqX#   save/sample2_tfidf_freq_tword20_a05qX   caption_modelqX	   show_tellqX   gpu_idqK X
   input_dataqX   data/coco/cocotalkqX
   train_onlyqKX   upsampling_sizeqM,X
   batch_sizeqK
X   seq_per_imgqKX   fliplrqK X	   cnn_modelqX   resnet50qX   cnn_fc_featqX   fc7qX   cnn_att_featqX   pool5qX
   cnn_weightqX    qX   pretrained_cnnq �X   fc_feat_sizeq!M X	   norm_featq"KX   rnn_sizeq#M X   rnn_biasq$K X
   num_layersq%KX   rnn_typeq&X   lstmq'X   input_encoding_sizeq(M X	   use_gloveq)K X	   drop_x_lmq*G?�      X   drop_prob_lmq+G?�      X   attend_modeq,X   concatq-X   num_regionsq.M X   att_feat_sizeq/M X
   scale_lossq0K X	   bootstrapq1K X   bootstrap_scoreq2X   ciderq3X   gt_loss_versionq4X   mlq5X   augmented_loss_versionq6h5X
   sample_capq7K X   sample_rewardq8KX   cider_dfq9X   data/coco-train-df.pq:X   clip_scoresq;K X   similarity_matrixq<X'   data/Glove/cocotalk_similarities_v2.pklq=X   loss_versionq>X   tfidfq?X   sentence_loss_versionq@KX   normalize_batchqAKX   bleu_versionqBX   softqCX   smooth_remove_equalqDK X   tau_wordqEG@4      X   word_add_entropyqFK X   tau_sentqGK X   clip_simqHK X	   exact_dklqIK X   limited_vocab_simqJK X   limited_vocab_subqKKX
   rare_tfidfqLKX   marginqMG?�ffffffX   alphaqNG?�      X   betaqOG?�������X   alpha_increase_everyqPKX   alpha_increase_factorqQG?�������X   alpha_speedqRM NX   alpha_strategyqSX   constantqTX   restartqUKX
   max_epochsqVKX	   grad_clipqWG?�������X   finetune_cnn_afterqXJ����X   finetune_cnn_onlyqYK X   optimqZX   adamq[X   optim_alphaq\G?陙����X
   optim_betaq]G?�����+X   optim_epsilonq^G>Ey��0�:X   weight_decayq_K X   learning_rateq`G?@bM���X   learning_rate_decay_startqaKX   lr_patienceqbKX   lr_strategyqcX   stepqdX   learning_rate_decay_everyqeKX   learning_rate_decay_rateqfG?�333333X	   cnn_optimqgh[X   cnn_optim_alphaqhG?陙����X   cnn_optim_betaqiG?�����+X   cnn_weight_decayqjK X   cnn_learning_rateqkG?�������X
   forbid_unkqlKX	   beam_sizeqmKX   val_images_useqnJ����X   save_checkpoint_everyqoM�X   language_creativityqpKX   language_evalqqKX   losses_log_everyqrKX   load_best_scoreqsKX   scheduled_sampling_startqtJ����X   scheduled_sampling_vocabquK X   scheduled_sampling_speedqvKdX!   scheduled_sampling_increase_everyqwKX    scheduled_sampling_increase_probqxG?�������X   scheduled_sampling_max_probqyG?�      X   scheduled_sampling_strategyqzhdX   match_pairsq{K X	   eventnameq|X%   events/sample2_tfidf_freq_tword20_a05q}X   loggerq~NX
   vocab_sizeqM%X
   seq_lengthq�KX   lr_waitq�K X
   current_lrq�G?'��9��X   scale_lrq�G?�
=p��
u}q�(X   Bleu_1q�G?�Z�=D�X   Bleu_2q�G?�tئ�"(X   Bleu_3q�G?�Qk,�X   Bleu_4q�G?�؏mX   ROUGE_Lq�cnumpy.core.multiarray
scalar
q�cnumpy
dtype
q�X   f8q�K K�q�Rq�(KX   <q�NNNJ����J����K tq�bCk�%eO�?q��q�Rq�X   CIDErq�h�h�C�iک�\�?q��q�Rq�X   SPICEq�h�h�C��[  �?q��q�Rq�X	   vocab_useq�MX   creative 3gramsq�G?w�=OnX   creative 4gramsq�G?�41�d�FX   creative 5gramsq�G?���B�X   ml_lossq�G@�Yp���uea]q�]q�(}q�(hKhKhG?�      hK hK h	X+   save/word2_tword015_CocoGlove_a02/model.pthq�h
X(   config/word2_tword015_CocoGlove_a02.yamlq�hX!   save/word2_tword015_CocoGlove_a02q�hX	   show_tellq�hKhX   data/coco/cocotalkq�hKhM,hK
hKhK hX   resnet50q�hX   fc7q�hX   pool5q�hhh �h!M h"Kh#M h$K h%Kh&X   lstmq�h(M h)K h*G?�      h+G?�      h,X   concatq�h.M h/M h0K h1K h2X   ciderq�h4X   mlq�h6h�X
   alter_lossq�K h7Kh8K h9X   data/coco-train-df.pq�h;K h<X&   data/Glove/train_coco_similarities.pklq�h>X   word2q�h@KhAKhBX   softq�hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK X   ngram_lengthq�KhMG?�ffffffhNG?ə�����hOG?�������hPKhQG?�������hRM NhSX   constantq�hUKhVKhWG?�������hXJ����hYK hZX   adamq�h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepq�heKhfG?�333333hgh�hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzh�h{K h|X#   events/word2_tword015_CocoGlove_a02q�h~NhM%h�Kh�K X   cnn_start_fromq�X/   save/word2_tword015_CocoGlove_a02/model-cnn.pthq�X   infos_start_fromq�X+   save/word2_tword015_CocoGlove_a02/infos.pklq�X   optimizer_start_fromq�X/   save/word2_tword015_CocoGlove_a02/optimizer.pthq�h�G?'��9��h�G?�
=p��
u}q�(X   Bleu_1q�G?�Vમ�X   Bleu_2q�G?�r��t��X   Bleu_3q�G?�BFw��X   Bleu_4q�G?�r�y��X   ROUGE_Lq�h�h�C�j'KD�?qƆq�Rq�X   CIDErq�h�h�C
g�m�?qʆq�Rq�X   SPICEq�h�h�CB	���?qΆq�Rq�X	   vocab_useq�M�X   creative 3gramsq�G?x��W�X   creative 4gramsq�G?�7����X   creative 5gramsq�G?�k�]d��h�G@���Kƨuea]q�]q�(}q�(hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a03.yamlq�hX!   save/word2_tword015_CocoGlove_a03q�hX	   show_tellq�hK hX   data/coco/cocotalkq�hKhM,hK
hKhK hX   resnet50q�hX   fc7q�hX   pool5q�hhh �h!M h"Kh#M h$K h%Kh&X   lstmq�h(M h)K h*G?�      h+G?�      h,X   concatq�h.M h/M h0K h1K h2X   ciderq�h4X   mlq�h6h�h�K h7Kh8K h9X   data/coco-train-df.pq�h;K h<X&   data/Glove/train_coco_similarities.pklq�h>X   word2q�h@KhAKhBX   softq�hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�333333hOG?�������hPKhQG?�������hRM NhSX   constantq�hUKhVKhWG?�������hXJ����hYK hZX   adamq�h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepq�heKhfG?�333333hgh�hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzh�h{K h|X#   events/word2_tword015_CocoGlove_a03q�h~NhM%h�Kh�K h�G?@bM���h�Ku}q�(X   Bleu_1q�G?��i��EX   Bleu_2q�G?�J�8�X   Bleu_3q�G?�t�2X   Bleu_4q�G?�8h[��X   ROUGE_Lq�h�h�C��\Y�?q�q�Rq�X   CIDErq�h�h�C�������?q��q�Rq�X   SPICEq�h�h�C��5�?q��q�Rq�X	   vocab_useq�MQX   creative 3gramsq�G?yL��pX   creative 4gramsq�G?��˕�\�X   creative 5gramsq�G?���~��,h�G@�Zn��uea]r   ]r  (}r  (hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a04.yamlr  hX!   save/word2_tword015_CocoGlove_a04r  hX	   show_tellr  hKhX   data/coco/cocotalkr  hKhM,hK
hKhK hX   resnet50r  hX   fc7r  hX   pool5r	  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr
  h(M h)K h*G?�      h+G?�      h,X   concatr  h.M h/M h0K h1K h2X   ciderr  h4X   mlr  h6j  h�K h7Kh8K h9X   data/coco-train-df.pr  h;K h<X&   data/Glove/train_coco_similarities.pklr  h>X   word2r  h@KhAKhBX   softr  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?ٙ�����hOG?�������hPKhQG?�������hRM NhSX   constantr  hUKhVKhWG?�������hXJ����hYK hZX   adamr  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr  heKhfG?�333333hgj  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj  h{K h|X#   events/word2_tword015_CocoGlove_a04r  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}r  (X   Bleu_1r  G?�#����X   Bleu_2r  G?��D7�X   Bleu_3r  G?؍e�çX   Bleu_4r  G?�Q��%�X   ROUGE_Lr  h�h�C����O�?r  �r  Rr  X   CIDErr  h�h�C@�r�B��?r   �r!  Rr"  X   SPICEr#  h�h�C�Ӽ��(�?r$  �r%  Rr&  X	   vocab_user'  M�X   creative 3gramsr(  G?r�%LJ��X   creative 4gramsr)  G?�'Ї^�X   creative 5gramsr*  G?�@�c�_�h�G@�1���uea]r+  ]r,  (}r-  (hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a05.yamlr.  hX!   save/word2_tword015_CocoGlove_a05r/  hX	   show_tellr0  hK hX   data/coco/cocotalkr1  hKhM,hK
hKhK hX   resnet50r2  hX   fc7r3  hX   pool5r4  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr5  h(M h)K h*G?�      h+G?�      h,X   concatr6  h.M h/M h0K h1K h2X   ciderr7  h4X   mlr8  h6j8  h�K h7Kh8K h9X   data/coco-train-df.pr9  h;K h<X&   data/Glove/train_coco_similarities.pklr:  h>X   word2r;  h@KhAKhBX   softr<  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�      hOG?�������hPKhQG?�������hRM NhSX   constantr=  hUKhVKhWG?�������hXJ����hYK hZX   adamr>  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr?  heKhfG?�333333hgj>  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj?  h{K h|X#   events/word2_tword015_CocoGlove_a05r@  h~NhM%h�Kh�K h�G?����f�h�G?������u}rA  (X   Bleu_1rB  G?�2�U�%�X   Bleu_2rC  G?���C4X   Bleu_3rD  G?؊W��d�X   Bleu_4rE  G?�0a��*�X   ROUGE_LrF  h�h�C���	�B�?rG  �rH  RrI  X   CIDErrJ  h�h�C�iE)��?rK  �rL  RrM  X   SPICErN  h�h�CEҟ�?rO  �rP  RrQ  X	   vocab_userR  MzX   creative 3gramsrS  G?l`o���$X   creative 4gramsrT  G?�xɡ5kPX   creative 5gramsrU  G?���xJ+h�G@
$e���uea]rV  ]rW  (}rX  (hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a06.yamlrY  hX!   save/word2_tword015_CocoGlove_a06rZ  hX	   show_tellr[  hK hX   data/coco/cocotalkr\  hKhM,hK
hKhK hX   resnet50r]  hX   fc7r^  hX   pool5r_  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr`  h(M h)K h*G?�      h+G?�      h,X   concatra  h.M h/M h0K h1K h2X   ciderrb  h4X   mlrc  h6jc  h�K h7Kh8K h9X   data/coco-train-df.prd  h;K h<X&   data/Glove/train_coco_similarities.pklre  h>X   word2rf  h@KhAKhBX   softrg  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�333333hOG?�������hPKhQG?�������hRM NhSX   constantrh  hUKhVKhWG?�������hXJ����hYK hZX   adamri  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   steprj  heKhfG?�333333hgji  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzjj  h{K h|X#   events/word2_tword015_CocoGlove_a06rk  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}rl  (X   Bleu_1rm  G?�H����X   Bleu_2rn  G?൝
�sUX   Bleu_3ro  G?؟�y��"X   Bleu_4rp  G?�1o7U�X   ROUGE_Lrq  h�h�CE *ƃR�?rr  �rs  Rrt  X   CIDErru  h�h�Csĺ���?rv  �rw  Rrx  X   SPICEry  h�h�C��|���?rz  �r{  Rr|  X	   vocab_user}  MgX   creative 3gramsr~  G?p����X   creative 4gramsr  G?�w��&X   creative 5gramsr�  G?��Y���h�G@�ּ(��uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a07.yamlr�  hX!   save/word2_tword015_CocoGlove_a07r�  hX	   show_tellr�  hK hX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M h)K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X&   data/Glove/train_coco_similarities.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�ffffffhOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X#   events/word2_tword015_CocoGlove_a07r�  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}r�  (X   Bleu_1r�  G?�Q�5Q�^X   Bleu_2r�  G?�ϧP-�X   Bleu_3r�  G?ج��jHfX   Bleu_4r�  G?�DMUχ�X   ROUGE_Lr�  h�h�C`/���]�?r�  �r�  Rr�  X   CIDErr�  h�h�C�j��y��?r�  �r�  Rr�  X   SPICEr�  h�h�C��L����?r�  �r�  Rr�  X	   vocab_user�  MVX   creative 3gramsr�  G?r��?�}X   creative 4gramsr�  G?���&�D�X   creative 5gramsr�  G?�,�`M(�h�G@
�Zz��uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X(   config/word2_tword015_CocoGlove_a08.yamlr�  hX!   save/word2_tword015_CocoGlove_a08r�  hX	   show_tellr�  hK hX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M h)K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X&   data/Glove/train_coco_similarities.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?陙����hOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X#   events/word2_tword015_CocoGlove_a08r�  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}r�  (X   Bleu_1r�  G?�s����X   Bleu_2r�  G?��SX�X   Bleu_3r�  G?����`�X   Bleu_4r�  G?ҥ�u�$&X   ROUGE_Lr�  h�h�C�z�7z�?r�  �r�  Rr�  X   CIDErr�  h�h�C�S1[Eq�?r�  �r�  Rr�  X   SPICEr�  h�h�C���!�?r�  �r�  Rr�  X	   vocab_user�  M*X   creative 3gramsr�  G?mA�A�X   creative 4gramsr�  G?�*Jq��X   creative 5gramsr�  G?��`�:��h�G@֬�O�;uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X'   config/word2_tword015_CocoGlove_a1.yamlr�  hX    save/word2_tword015_CocoGlove_a1r�  hX	   show_tellr�  hKhX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M h)K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X&   data/Glove/train_coco_similarities.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?�333333hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�      hOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X"   events/word2_tword015_CocoGlove_a1r�  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}r�  (X   Bleu_1r�  G?�Z�Ј��X   Bleu_2r�  G?�b��.RX   Bleu_3r�  G?�1�38�/X   Bleu_4r�  G?�-�)�8MX   ROUGE_Lr�  h�h�C{f�8}�?r�  �r�  Rr�  X   CIDErr�  h�h�C�9�4c�?r�  �r�  Rr�  X   SPICEr�  h�h�C����Q�?r�  �r�  Rr�  X	   vocab_user�  M]X   creative 3gramsr�  G?���J�wX   creative 4gramsr   G?�a{��X   creative 5gramsr  G?ȸ�l�īh�G@��+uea]r  ]r  (}r  (hKhKhG?�      hK hK h	Nh
X   config/word2_tword01_a03.yamlr  hX   save/word2_tword01_a03r  hX	   show_tellr  hKhX   data/coco/cocotalkr  hKhM,hK
hKhK hX   resnet50r	  hX   fc7r
  hX   pool5r  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr  h(M h)K h*G?�      h+G?�      h,X   concatr  h.M h/M h0K h1K h2X   ciderr  h4X   mlr  h6j  h7Kh<X'   data/Glove/cocotalk_similarities_v2.pklr  h>X   word2r  hBX   softr  hDK hEG?�������hGK hHK hJK hMG?�ffffffhNG?�333333hOG?�������hPKhQG?�������hRM NhSX   constantr  hUKhVJ����hWG?�������hXJ����hYK hZX   adamr  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr  heKhfG?�333333hgj  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj  h{K h|X   events/word2_tword01_a03r  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}r  (X   Bleu_1r  G?�|���IX   Bleu_2r  G?�j���y�X   Bleu_3r  G?�0U J%X   Bleu_4r  G?��>Y��X   ROUGE_Lr  h�h�C��6�?r  �r  Rr  X   CIDErr   h�h�C�¢�zx�?r!  �r"  Rr#  X   SPICEr$  h�h�C���.�?r%  �r&  Rr'  X	   vocab_user(  M�X   creative 3gramsr)  G?o��3�w�X   creative 4gramsr*  G?�����X   creative 5gramsr+  G?�ժs�h�K uea]r,  ]r-  (}r.  (hKhKhG?�      hK hK h	Nh
X%   config/word2_tword01_a09_entropy.yamlr/  hX   save/word2_tword01_a09_entropyr0  hX	   show_tellr1  hK hX   data/coco/cocotalkr2  hKhM,hK
hKhK hX   resnet50r3  hX   fc7r4  hX   pool5r5  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr6  h(M h)K h*G?�      h+G?�      h,X   concatr7  h.M h/M h0K h1K h2X   ciderr8  h4X   mlr9  h6j9  h7Kh<X'   data/Glove/cocotalk_similarities_v2.pklr:  h>X   word2r;  hBX   softr<  hDK hEG?�������hFKhGK hHK hJK hMG?�ffffffhNG?�������hOG?�������hPKhQG?�������hRM NhSX   constantr=  hUKhVJ����hWG?�������hXJ����hYK hZX   adamr>  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr?  heKhfG?�333333hgj>  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj?  h{K h|X    events/word2_tword01_a09_entropyr@  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}rA  (X   Bleu_1rB  G?�qV�)\X   Bleu_2rC  G?��3����X   Bleu_3rD  G?���$F}X   Bleu_4rE  G?҉���QX   ROUGE_LrF  h�h�C�̈zi�?rG  �rH  RrI  X   CIDErrJ  h�h�C�n���?rK  �rL  RrM  X   SPICErN  h�h�C9�l�E��?rO  �rP  RrQ  X	   vocab_userR  M�X   creative 3gramsrS  G?qM[�X   creative 4gramsrT  G?����X   creative 5gramsrU  G?��8�M�_h�K uea]rV  ]rW  (}rX  (hKhKhG?�      hK hK h	Nh
X$   config/word2_tword01_a1_entropy.yamlrY  hX   save/word2_tword01_a1_entropyrZ  hX	   show_tellr[  hK hX   data/coco/cocotalkr\  hKhM,hK
hKhK hX   resnet50r]  hX   fc7r^  hX   pool5r_  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr`  h(M h)K h*G?�      h+G?�      h,X   concatra  h.M h/M h0K h1K h2X   ciderrb  h4X   mlrc  h6jc  h7Kh<X'   data/Glove/cocotalk_similarities_v2.pklrd  h>X   word2re  hBX   softrf  hDK hEG?�������hFKhGK hHK hJK hMG?�ffffffhNG?�      hOG?�������hPKhQG?�������hRM NhSX   constantrg  hUKhVJ����hWG?�������hXJ����hYK hZX   adamrh  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepri  heKhfG?�333333hgjh  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzji  h{K h|X   events/word2_tword01_a1_entropyrj  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}rk  (X   Bleu_1rl  G?�RQ9�bX   Bleu_2rm  G?ߵ<�SK�X   Bleu_3rn  G?։�( bX   Bleu_4ro  G?�
�[�8X   ROUGE_Lrp  h�h�C�l9_���?rq  �rr  Rrs  X   CIDErrt  h�h�C@�g�y�?ru  �rv  Rrw  X   SPICErx  h�h�C�Iw�?ry  �rz  Rr{  X	   vocab_user|  MvX   creative 3gramsr}  G?��w�[��X   creative 4gramsr~  G?�|��w�cX   creative 5gramsr  G?����Îh�K uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X0   config/word2_tword025_CocoGloved512_w15_a09.yamlr�  hX)   save/word2_tword025_CocoGloved512_w15_a09r�  hX	   show_tellr�  hK hX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M X   init_decoder_Wr�  hX   freeze_decoder_Wr�  K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X/   data/Glove/glove_coco_d512_w15_similarities.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?�      hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�������hOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X+   events/word2_tword025_CocoGloved512_w15_a09r�  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}r�  (X   Bleu_1r�  G?��L�A�X   Bleu_2r�  G?����]/X   Bleu_3r�  G?�D��`�X   Bleu_4r�  G?Һ����8X   ROUGE_Lr�  h�h�C0���s}�?r�  �r�  Rr�  X   CIDErr�  h�h�C�:_Q�?r�  �r�  Rr�  X   SPICEr�  h�h�C����+�?r�  �r�  Rr�  X	   vocab_user�  M�X   creative 3gramsr�  G?m�#�(�X   creative 4gramsr�  G?����>�0X   creative 5gramsr�  G?�oF�oF�h�G@���"�uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X   config/word2_tword02_a02.yamlr�  hX   save/word2_tword02_a02r�  hX	   show_tellr�  hKhX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M j�  hj�  K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X'   data/Glove/cocotalk_similarities_v2.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?ə�����hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?ə�����hOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X   events/word2_tword02_a02r�  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}r�  (X   Bleu_1r�  G?��9G!1�X   Bleu_2r�  G?�_�د�X   Bleu_3r�  G?�&E%���X   Bleu_4r�  G?����vX   ROUGE_Lr�  h�h�C��Y��.�?r�  �r�  Rr�  X   CIDErr�  h�h�C�L\�qJ�?r�  �r�  Rr�  X   SPICEr�  h�h�C�����?r�  �r�  Rr�  X	   vocab_user�  M�X   creative 3gramsr�  G?iyw{�X   creative 4gramsr�  G?�sB���KX   creative 5gramsr�  G?������h�G@�����`uea]r�  ]r�  (}r�  (hKhKhG?�      hK hK h	Nh
X   config/word2_tword02_a03.yamlr�  hX   save/word2_tword02_a03r�  hX	   show_tellr�  hK hX   data/coco/cocotalkr�  hKhM,hK
hKhK hX   resnet50r�  hX   fc7r�  hX   pool5r�  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr�  h(M j�  hj�  K h*G?�      h+G?�      h,X   concatr�  h.M h/M h0K h1K h2X   ciderr�  h4X   mlr�  h6j�  h�K h7Kh8K h9X   data/coco-train-df.pr�  h;K h<X'   data/Glove/cocotalk_similarities_v2.pklr�  h>X   word2r�  h@KhAKhBX   softr�  hDK hEG?ə�����hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�333333hOG?�������hPKhQG?�������hRM NhSX   constantr�  hUKhVKhWG?�������hXJ����hYK hZX   adamr�  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr�  heKhfG?�333333hgj�  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj�  h{K h|X   events/word2_tword02_a03r�  h~NhM%h�Kh�K h�G?O��3 �h�G?˥�S���u}r�  (X   Bleu_1r�  G?��ny�X   Bleu_2r�  G?��![��X   Bleu_3r�  G?�T�_��X   Bleu_4r�  G?�"ಘ�X   ROUGE_Lr�  h�h�C<w;{H�?r�  �r�  Rr�  X   CIDErr�  h�h�C#��s8��?r�  �r�  Rr�  X   SPICEr�  h�h�C|��B_��?r�  �r�  Rr�  X	   vocab_user�  M�X   creative 3gramsr   G?p�lX   creative 4gramsr  G?�1����X   creative 5gramsr  G?�u����ch�G@�}�bM�uea]r  ]r  (}r  (hKhKhG?�      hK hK h	Nh
X   config/word2_tword02_a04.yamlr  hX   save/word2_tword02_a04r  hX	   show_tellr  hKhX   data/coco/cocotalkr	  hKhM,hK
hKhK hX   resnet50r
  hX   fc7r  hX   pool5r  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr  h(M j�  hj�  K h*G?�      h+G?�      h,X   concatr  h.M h/M h0K h1K h2X   ciderr  h4X   mlr  h6j  h�K h7Kh8K h9X   data/coco-train-df.pr  h;K h<X'   data/Glove/cocotalk_similarities_v2.pklr  h>X   word2r  h@KhAKhBX   softr  hDK hEG?ə�����hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?ٙ�����hOG?�������hPKhQG?�������hRM NhSX   constantr  hUKhVKhWG?�������hXJ����hYK hZX   adamr  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   stepr  heKhfG?�333333hgj  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzj  h{K h|X   events/word2_tword02_a04r  h~NhM%h�Kh�K h�G?����f�h�G?������u}r  (X   Bleu_1r  G?�'p��CmX   Bleu_2r  G?��.����X   Bleu_3r  G?�{ Ϧj�X   Bleu_4r  G?�51���X   ROUGE_Lr  h�h�C��OE�?r  �r   Rr!  X   CIDErr"  h�h�C����,��?r#  �r$  Rr%  X   SPICEr&  h�h�C��0��?r'  �r(  Rr)  X	   vocab_user*  M�X   creative 3gramsr+  G?p���%��X   creative 4gramsr,  G?��p�s�X   creative 5gramsr-  G?��]���Vh�G@�dӕ�uea]r.  ]r/  (}r0  (hKhKhG?�      hK hK h	Nh
X   config/word2_tword02_a05.yamlr1  hX   save/word2_tword02_a05r2  hX	   show_tellr3  hK hX   data/coco/cocotalkr4  hKhM,hK
hKhK hX   resnet50r5  hX   fc7r6  hX   pool5r7  hhh �h!M h"Kh#M h$K h%Kh&X   lstmr8  h(M h)K h*G?�      h+G?�      h,X   concatr9  h.M h/M h0K h1K h2X   ciderr:  h4X   mlr;  h6j;  h�K h7Kh8K h9X   data/coco-train-df.pr<  h;K h<X'   data/Glove/cocotalk_similarities_v2.pklr=  h>X   word2r>  h@KhAKhBX   softr?  hDK hEG?ə�����hFK hGK hHK hIK hJK hKKhLK h�KhMG?�ffffffhNG?�      hOG?�������hPKhQG?�������hRM NhSX   constantr@  hUKhVKhWG?�������hXJ����hYK hZX   adamrA  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   steprB  heKhfG?�333333hgjA  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzjB  h{K h|X   events/word2_tword02_a05rC  h~NhM%h�Kh�K h�G?@bM���h�Ku}rD  (X   Bleu_1rE  G?��](��X   Bleu_2rF  G?�/��i�X   Bleu_3rG  G?мD�Ö�X   Bleu_4rH  G?��L�oX   ROUGE_LrI  h�h�Cu˅����?rJ  �rK  RrL  X   CIDErrM  h�h�CB�*�/�?rN  �rO  RrP  X   SPICErQ  h�h�CV,^:�?rR  �rS  RrT  X	   vocab_userU  K�X   creative 3gramsrV  G?g�xq�X   creative 4gramsrW  G?�4K���X   creative 5gramsrX  G?�_>��)�h�G@o�rI�uea]rY  ]rZ  (}r[  (hKhKhG?�      hK hK h	Nh
X%   config/word2_tword05_a03_entropy.yamlr\  hX   save/word2_tword05_a03_entropyr]  hX	   show_tellr^  hK hX   data/coco/cocotalkr_  hKhM,hK
hKhK hX   resnet50r`  hX   fc7ra  hX   pool5rb  hhh �h!M h"Kh#M h$K h%Kh&X   lstmrc  h(M h)K h*G?�      h+G?�      h,X   concatrd  h.M h/M h0K h1K h2X   ciderre  h4X   mlrf  h6jf  h7Kh<X'   data/Glove/cocotalk_similarities_v2.pklrg  h>X   word2rh  hBX   softri  hDK hEG?�      hFKhGK hHK hJK hMG?�ffffffhNG?�333333hOG?�������hPKhQG?�������hRM NhSX   constantrj  hUKhVJ����hWG?�������hXJ����hYK hZX   adamrk  h\G?陙����h]G?�����+h^G>Ey��0�:h_K h`G?@bM���haKhbKhcX   steprl  heKhfG?�333333hgjk  hhG?陙����hiG?�����+hjK hkG?�������hlKhmKhnJ����hoM�hpKhqKhrKhsKhtJ����huK hvKdhwKhxG?�������hyG?�      hzjl  h{K h|X    events/word2_tword05_a03_entropyrm  h~NhM%h�Kh�K h�G?'��9��h�G?�
=p��
u}rn  (X   Bleu_1ro  G?���+��X   Bleu_2rp  G?����T�wX   Bleu_3rq  G?�Y��]�dX   Bleu_4rr  G?�#/�V�X   ROUGE_Lrs  h�h�C
/^NI�?rt  �ru  Rrv  X   CIDErrw  h�h�Cj��0��?rx  �ry  Rrz  X   SPICEr{  h�h�C02�4U�?r|  �r}  Rr~  X	   vocab_user  M�X   creative 3gramsr�  G?r=ŋ�#�X   creative 4gramsr�  G?��`�2vX   creative 5gramsr�  G?�����h�K ueae.