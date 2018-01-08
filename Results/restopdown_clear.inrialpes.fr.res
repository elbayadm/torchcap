�]q (]q]q(}q(X
   beams_sizeqKX
   sample_maxqKX   temperatureqG?�      X   flipqK X   start_from_bestqK X
   start_fromq	NX   reset_optimizerq
K X   shift_epochqK X   configqX"   config/topdown_resnet152_bs20.yamlqX	   modelnameqX   save/topdown_resnet152_bs20qX   caption_modelqX   top_downqX   gpu_idqK X
   input_dataqX   data/coco/cocotalkqX
   train_onlyqKX   upsampling_sizeqM,X
   batch_sizeqKX   seq_per_imgqKX   fliplrqK X	   cnn_modelqX	   resnet152qX   cnn_fc_featqX   fc7qX   cnn_att_featqX   pool5qX
   cnn_weightq X    q!X   pretrained_cnnq"�X   fc_feat_sizeq#M X	   norm_featq$KX   rnn_sizeq%M X   rnn_biasq&K X
   num_layersq'KX   rnn_typeq(X   lstmq)X   input_encoding_sizeq*M X   init_decoder_Wq+h!X   freeze_decoder_Wq,K X	   drop_x_lmq-G?�      X   drop_prob_lmq.G?�      X   drop_feat_imq/G        X   drop_sentinelq0G?�      X   attend_modeq1X   concatq2X   region_sizeq3KX   att_feat_sizeq4M X   att_hid_sizeq5M X   use_adaptive_poolingq6K X
   use_maxoutq7K X
   add_fc_imgq8KX
   scale_lossq9K X   scale_wlq:K X	   bootstrapq;K X   bootstrap_scoreq<X   ciderq=X   gt_loss_versionq>X   mlq?X   augmented_loss_versionq@h?X
   alter_lossqAK X
   alter_modeqBX   even-oddqCX   sum_lossqDK X   combine_lossqEK X
   sample_capqFK X   sample_rewardqGK X   cider_dfqHX   data/coco-train-df.pqIX   clip_scoresqJK X   similarity_matrixqKX'   data/Glove/cocotalk_similarities_v2.pklqLX   use_coocqMK X   loss_versionqNX   wordqOX   sentence_loss_versionqPKX
   mc_samplesqQKX   normalize_batchqRKX   bleu_versionqSX   softqTX   smooth_remove_equalqUK X   tau_wordqVG?tz�G�{X   word_add_entropyqWK X   tau_sentqXK X   clip_simqYK X	   exact_dklqZK X   limited_vocab_simq[K X   limited_vocab_subq\KX
   rare_tfidfq]K X   sub_idfq^K X   ngram_lengthq_KX   marginq`G?�ffffffX
   alpha_sentqaG?ٙ�����X
   alpha_wordqbG?�������X   betaqcG?�������X   gammaqdG?��Q�X   alpha_increase_everyqeKX   alpha_increase_factorqfG?�������X	   alpha_maxqgG?�������X   alpha_increase_startqhKX   alpha_speedqiM NX   alpha_strategyqjX   constantqkX   verboseqlK X   restartqmKX
   max_epochsqnKX	   grad_clipqoG?�������X   finetune_cnn_afterqpJ����X   finetune_cnn_onlyqqK X   finetune_cnn_sliceqrK X   optimqsX   adamqtX   optim_alphaquG?陙����X
   optim_betaqvG?�����+X   optim_epsilonqwG>Ey��0�:X   weight_decayqxK X   learning_rateqyG?:6��C-X   learning_rate_decay_startqzKX   lr_patienceq{KX   lr_strategyq|X   stepq}X   learning_rate_decay_everyq~KX   learning_rate_decay_rateqG?�333333X	   cnn_optimq�htX   cnn_optim_alphaq�G?陙����X   cnn_optim_betaq�G?�����+X   cnn_weight_decayq�K X   cnn_learning_rateq�G?�������X
   forbid_unkq�KX	   beam_sizeq�KX   val_images_useq�J����X   save_checkpoint_everyq�M�X   language_creativityq�KX   language_evalq�KX   losses_log_everyq�KX   load_best_scoreq�KX   scheduled_sampling_startq�J����X   scheduled_sampling_vocabq�K X   scheduled_sampling_speedq�KdX!   scheduled_sampling_increase_everyq�KX    scheduled_sampling_increase_probq�G?�������X   scheduled_sampling_max_probq�G?�      X   scheduled_sampling_strategyq�h}X   match_pairsq�K X	   eventnameq�X   events/topdown_resnet152_bs20q�X   loggerq�NX
   vocab_sizeq�M%X
   seq_lengthq�KX   lr_waitq�K X
   current_lrq�G? N�M\ݮX   scale_lrq�G?��P�ܛu}q�(X   Bleu_1q�G?�,�:X   Bleu_2q�G?�ᆙ�~X   Bleu_3q�G?ڠ�q�MqX   Bleu_4q�G?�)_�,�X   CIDErq�cnumpy.core.multiarray
scalar
q�cnumpy
dtype
q�X   f8q�K K�q�Rq�(KX   <q�NNNJ����J����K tq�bC��D"���?q��q�Rq�X	   vocab_useq�M�X   creative 3gramsq�G?�E�4��)X   creative 4gramsq�G?�����I:X   creative 5gramsq�G?�(��]�X	   best/lastq�X	   64k / 84kq�X   ml_lossq�G@{���+uea]q�]q�(}q�(hKhKhG?�      hK hK h	Nh
K hK hX+   config/topdown_resnet152_genconf15_msc.yamlq�hX$   save/topdown_resnet152_genconf15_mscq�hX   top_downq�hK hX   data/coco/genConf_cocotalkq�hKhM,hK
hKhK hX	   resnet152q�hX   fc7q�hX   pool5q�h h!h"�h#M h$Kh%M h&K h'Kh(X   lstmq�h*M h+h!h,K h-G?�      h.G?�      h/G        h0G?�      h1X   concatq�h3Kh4M h5M h6K h7K h8Kh9K h:K h;K h<X   ciderq�h>X   mlq�h@h�hAK hBX   even-oddq�hDK hEK hFK hGK hHX   data/coco-train-df.pq�hJK hKX'   data/Glove/cocotalk_similarities_v2.pklq�hMK hNX   wordq�hPKhQKhRKhSX   softq�hUK hVG?tz�G�{hWK hXK hYK hZK h[K h\Kh]K h^K h_Kh`G?�ffffffhaG?ٙ�����hbG?�������hcG?�������hdG?��Q�heKhfG?�������hgG?�������hhKhiM NhjX   constantq�hlK hmKhnKhoG?�������hpJ����hqK hrK hsX   adamq�huG?陙����hvG?�����+hwG>Ey��0�:hxK hyG?:6��C-hzKh{Kh|X   stepq�h~KhG?�333333h�h�h�G?陙����h�G?�����+h�K h�G?�������h�Kh�Kh�J����h�M�h�Kh�Kh�Kh�Kh�J����h�K h�Kdh�Kh�G?�������h�G?�      h�h�h�K h�X&   events/topdown_resnet152_genconf15_mscq�h�Nh�M%h�Kh�K h�G? N�M\ݮh�G?��P�ܛu}q�(X   Bleu_1q�G?��tWkX   Bleu_2q�G?�S���X   Bleu_3q�G?ۉ0����X   Bleu_4q�G?�k�v��
X   CIDErq�h�h�C%��d�8�?qцq�Rq�X	   vocab_useq�M�X   creative 3gramsq�G?��}��U>X   creative 4gramsq�G?�}����AX   creative 5gramsq�G?�ŗW�1�h�X   116k / 168kq�h�G@6 9Xuea]q�]q�(}q�(hKhKhG?�      hK hK h	Nh
K hK hX!   config/topdown_resnet152_msc.yamlq�hX   save/topdown_resnet152_mscq�hX   top_downq�hK hX   data/coco/cocotalkq�hKhM,hK
hKhK hX	   resnet152q�hX   fc7q�hX   pool5q�h h!h"�h#M h$Kh%M h&K h'Kh(X   lstmq�h*M h+h!h,K h-G?�      h.G?�      h/G        h0G?�      h1X   concatq�h3Kh4M h5M h6K h7K h8Kh9K h:K h;K h<X   ciderq�h>X   mlq�h@h�hAK hBX   even-oddq�hDK hEK hFK hGK hHX   data/coco-train-df.pq�hJK hKX'   data/Glove/cocotalk_similarities_v2.pklq�hMK hNX   wordq�hPKhQKhRKhSX   softq�hUK hVG?tz�G�{hWK hXK hYK hZK h[K h\Kh]K h^K h_Kh`G?�ffffffhaG?ٙ�����hbG?�������hcG?�������hdG?��Q�heKhfG?�������hgG?�������hhKhiM NhjX   constantq�hlK hmKhnKhoG?�������hpJ����hqK hrK hsX   adamq�huG?陙����hvG?�����+hwG>Ey��0�:hxK hyG?:6��C-hzKh{Kh|X   stepq�h~KhG?�333333h�h�h�G?陙����h�G?�����+h�K h�G?�������h�Kh�Kh�J����h�M�h�Kh�Kh�Kh�Kh�J����h�K h�Kdh�Kh�G?�������h�G?�      h�h�h�K h�X   events/topdown_resnet152_mscq�h�Nh�M%h�Kh�K h�G? N�M\ݮh�G?��P�ܛu}q�(X   Bleu_1q�G?��,��X   Bleu_2q�G?�6��|X   Bleu_3q�G?ڍX�)�/X   Bleu_4q�G?���J�&�X   CIDErq�h�h�Cf�+�b��?q��q�Rq�X	   vocab_useq�M�X   creative 3gramsq�G?�-l����X   creative 4gramsq�G?�|���X   creative 5gramsq�G?�,�e��h�X   116k / 172kq�h�G@��gueae.