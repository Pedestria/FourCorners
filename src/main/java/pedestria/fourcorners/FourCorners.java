package pedestria.fourcorners;

import com.mojang.logging.LogUtils;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.slf4j.Logger;
import pedestria.fourcorners.registry.FCBlockEntities;
import pedestria.fourcorners.registry.FCBlocks;
import pedestria.fourcorners.registry.FCCreativeTabs;
import pedestria.fourcorners.registry.FCItems;
import pedestria.fourcorners.registry.FCMenus;

@Mod(FourCorners.MODID)
public final class FourCorners {
    public static final String MODID = "fourcorners";
    public static final Logger LOGGER = LogUtils.getLogger();

    public FourCorners() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();

        FCBlocks.BLOCKS.register(modEventBus);
        FCItems.ITEMS.register(modEventBus);
        FCCreativeTabs.CREATIVE_MODE_TABS.register(modEventBus);
        FCBlockEntities.BLOCK_ENTITY_TYPES.register(modEventBus);
        FCMenus.MENUS.register(modEventBus);
    }
}
