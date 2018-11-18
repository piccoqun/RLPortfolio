from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import pandas as pd
from lib.gftTools import gftIO

class HistoryManager:
    def __init__(self, file_path='database/data.pkl'):
        dic_data =  gftIO.zload(file_path)
        all_factors = list()
        columns = None

        for key, value in dic_data.items():
            if columns is None:
                columns = self._bin_o_set_2_str(value.columns.values)
            value.columns = columns
            all_factors.append(key)

        panel = pd.Panel(dic_data).transpose(0,2,1)
        # print(len(panel.major_axis), len(panel.minor_axis))
        # cutoff old data
        split_date = pd.to_datetime('20150701', format='%Y%m%d')
        panel = panel.loc[:,:,panel.minor_axis>=split_date]

        na_filled = panel.fillna(axis=2, method='ffill')
        panel_na_droped = na_filled.dropna(axis=1, how='any')
        self.panel = panel_na_droped

    def _bin_o_set_2_str(self, binary_gids):
        str_gid_list = list()
        for bin_gid in binary_gids:
            str_gid_list.append(gftIO.binary_to_str(bin_gid))
        return str_gid_list

    def get_global_data_matrix(self, start, end, features=('close',)):
        """
        :return a numpy ndarray whose axis is [feature, coin, time]
        """
        return self.get_global_panel(start, end, features).values

    def get_global_panel(self, start, end, features=('close',)):
        offset_4_gs_date = pd.Timestamp(start, unit='s').tz_localize(tz='Asia/Hong_Kong').tz._utcoffset.seconds
        start += offset_4_gs_date
        end += offset_4_gs_date
        panel = self.panel.loc[features,:,((self.panel.minor_axis >= pd.Timestamp(start,unit='s')) & (self.panel.minor_axis <= pd.Timestamp(end,unit='s')))]
        self.columns = panel.major_axis
        print("stocks:", len(panel.major_axis))
        print("periods:", len(panel.minor_axis))
        return panel

    def coins(self): # no use in everywhere
        return self.columns