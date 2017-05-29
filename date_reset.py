#Reset timestamps to have same range:
min_date = max([min(bullets_rem.index),
                min(bullets_hl.index),
                min(guns_rem.index),
                min(guns_hl.index)]
            )

max_date = min([max(bullets_rem.index),
                max(bullets_hl.index),
                max(guns_rem.index),
                max(guns_hl.index)]
            )

bullets_rem_trim = bullets_rem['1810-01-01':'1816-12-01']
bullets_hl_trim = bullets_hl['1810-01-01':'1816-12-01']

rem_model = bullets_rem.handgun_model.unique().tolist()
