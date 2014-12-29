<html>
<head>
<style type="text/css">
	${css} 
</style>
</head>
<body>
<% setLang(user.lang) %>
<div>
		<div>
				<div>
	
					## ${helper.embed_image('jpeg',str(get_partners(['form']['mov_type'])[0].company_id.logo_web),250, 120)}

				</div>
			<h3 class="title">
				${_('PARTNER BALANCE REPORT') | entity}
				
			</h3>
			<h5>
				<div align="center">
					<p>${_('FROM :')}${formatLang(data['form']['date_start'],date=True) | entity }${_('  TO :')}${formatLang(data['form']['date_finish'],date=True) | entity}</p>
				</div>
		
			</h5>
		</div>
</div>

    		
% for o in 	get_partners(data['form']['mov_type']):
	%if ( get_move_lines(data,o.id) != 0 ):
		<table  width="100%">	
							<tr>
									<td width="50%" align='center'>
										<font size="1">
											</div>${ o.name | entity }</div>
										</font>
									</td>
									<td width="50%" align='left' style="font-size:10px;">
										<font size="1">
								## %if o.currency_id:
								## 			${o.currency_id.name}
								## 			${_('TC:')}${"{0:.2f}".format(1/get_tc(o.currency_id.id,o.date))}
								## 			<br>
								## 			${'REF:'}${formatLang(o.amount_currency,monetary=True)}
								## %endif
										${_('Balance')}${' : '}${formatLang(get_move_lines(data,o.id),monetary=True)}

										</font>
									</td>
							</tr>
	%endif
%endfor

		</table>
			
<p style="page-break-before: always;"></p>
</body>
</html>