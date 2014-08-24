#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Audio 1 Top Block
# Author: Wylie Standage-Beier
# Description: Example of a low pass filter
# Generated: Sat Aug 23 16:33:14 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class audio_1_top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Audio 1 Top Block")
        _icon_path = "/usr/local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.freq_trans = freq_trans = 1e3
        self.freq_cutoff = freq_cutoff = 1e3
        self.freq = freq = 1e3

        ##################################################
        # Blocks
        ##################################################
        _freq_trans_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_trans_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_trans_sizer,
        	value=self.freq_trans,
        	callback=self.set_freq_trans,
        	label="Frequency transision window",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_trans_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_trans_sizer,
        	value=self.freq_trans,
        	callback=self.set_freq_trans,
        	minimum=0,
        	maximum=1e4,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_trans_sizer)
        _freq_cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_cutoff_sizer,
        	value=self.freq_cutoff,
        	callback=self.set_freq_cutoff,
        	label="Frequency Cut Off",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_cutoff_sizer,
        	value=self.freq_cutoff,
        	callback=self.set_freq_cutoff,
        	minimum=0,
        	maximum=1e4,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_cutoff_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label="Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=0,
        	maximum=1e4,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, freq_cutoff, freq_trans, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(samp_rate, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.freq_cutoff, self.freq_trans, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_freq_trans(self):
        return self.freq_trans

    def set_freq_trans(self, freq_trans):
        self.freq_trans = freq_trans
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.freq_cutoff, self.freq_trans, firdes.WIN_HAMMING, 6.76))
        self._freq_trans_slider.set_value(self.freq_trans)
        self._freq_trans_text_box.set_value(self.freq_trans)

    def get_freq_cutoff(self):
        return self.freq_cutoff

    def set_freq_cutoff(self, freq_cutoff):
        self.freq_cutoff = freq_cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.freq_cutoff, self.freq_trans, firdes.WIN_HAMMING, 6.76))
        self._freq_cutoff_slider.set_value(self.freq_cutoff)
        self._freq_cutoff_text_box.set_value(self.freq_cutoff)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq)
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = audio_1_top_block()
    tb.Start(True)
    tb.Wait()
