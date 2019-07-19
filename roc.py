from matplotlib import pyplot as plt
import numpy as np


def plot_roc_and_auc(tp_fp_file_name):
	casia_roc_data = open('mob on casia e1/' + tp_fp_file_name, 'r').readlines()
	vox_roc_data = open('mob on casia e2/' + tp_fp_file_name, 'r').readlines()

	# casia
	tp, fp = [], []
	casia_auc = 0
	for idx, data in enumerate(casia_roc_data):
		temp = data.split(',')
		tp.append(float(temp[0]))
		fp.append(float(temp[1]))

	casia_final_tp = np.mean(np.array(tp).reshape(-1, 10), axis=1)
	casia_final_fp = np.mean(np.array(fp).reshape(-1, 10), axis=1)

	for idx, data in enumerate(casia_final_tp[:-1]):
		distance = casia_final_fp[idx + 1] - casia_final_fp[idx]
		casia_auc += distance * casia_final_tp[idx + 1]

	# voxceleb
	tp, fp = [], []
	vox_auc = 0
	for idx, data in enumerate(vox_roc_data):
		temp = data.split(',')
		tp.append(float(temp[0]))
		fp.append(float(temp[1]))

	vox_final_tp = np.mean(np.array(tp).reshape(-1, 10), axis=1)
	vox_final_fp = np.mean(np.array(fp).reshape(-1, 10), axis=1)

	for idx, data in enumerate(vox_final_tp[:-1]):
		distance = vox_final_fp[idx + 1] - vox_final_fp[idx]
		vox_auc += distance * vox_final_tp[idx + 1]

	# Plot
	plt.figure(1)
	plt.plot([0, 1], [0, 1], 'k--', alpha=0.6)
	# plt.plot(vox_final_fp, vox_final_tp, '-ok')
	plt.plot(vox_final_fp, vox_final_tp, '-ok', c='b', label='casia e1 - AUC = {:.4f}'.format(casia_auc), markersize=2)
	plt.plot(casia_final_fp, casia_final_tp, '-ok', c='r', label='casia e2 - AUC = {:.4f}'.format(vox_auc), markersize=2)
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('ROC for ' + (tp_fp_file_name).upper())
	plt.legend()

	plt.figure(2)
	plt.plot(vox_final_fp, vox_final_tp, '-ok', c='b', label='casia e1 - AUC = {:.4f}'.format(casia_auc), markersize=2)
	plt.plot(casia_final_fp, casia_final_tp, '-ok', c='r', label='casia e2 - AUC = {:.4f}'.format(vox_auc), markersize=2)
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('ROC for ' + (tp_fp_file_name).upper() + ' - Zoomed on top-left')
	plt.xlim(0, 0.3)
	plt.ylim(0.7, 1)
	plt.legend()
	plt.show()


plot_roc_and_auc('ytf')
